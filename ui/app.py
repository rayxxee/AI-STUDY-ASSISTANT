import streamlit as st
import requests
import os

API_BASE = os.getenv("API_BASE", "http://localhost:5000")

st.set_page_config(page_title="AI Study Assistant", layout="wide")
st.title("📚 AI Study Assistant")

# Sidebar: Upload Document
with st.sidebar:
    st.header("📄 Knowledge Base")
    uploaded_file = st.file_uploader("Upload a study document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    
    if st.button("Process Document"):
        if uploaded_file is not None:
            with st.spinner("Ingesting document..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                try:
                    res = requests.post(f"{API_BASE}/upload", files=files)
                    if res.status_code == 200:
                        st.success("Successfully processed and stored in FAISS!")
                    else:
                        st.error(f"Error: {res.json().get('error', 'Unknown Error')}")
                except Exception as e:
                    st.error(f"Failed to connect to backend: {e}")
        else:
            st.warning("Please select a file first.")
            
    st.divider()
    st.subheader("Extract Insights")
    if st.button("Generate Summary"):
        with st.spinner("Analyzing knowledge base..."):
            try:
                res = requests.get(f"{API_BASE}/summarize")
                if res.status_code == 200:
                    st.info(res.json().get('summary', ''))
                else:
                    st.error(f"Error: {res.json().get('error', 'Unknown')}")
            except Exception as e:
                st.error(f"Failed to connect: {e}")

# Main Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "context" in message and message["context"]:
            with st.expander("View Source Citations"):
                for idx, ctx in enumerate(message["context"]):
                    st.markdown(f"**Chunk {idx+1}** (Distance: {ctx.get('distance', 'N/A')}):")
                    st.text(ctx.get('text', ''))

# Accept user input
if prompt := st.chat_input("Ask a question about your documents..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(f"{API_BASE}/query", json={"question": prompt})
                if res.status_code == 200:
                    data = res.json()
                    answer = data.get("answer", "No answer found.")
                    context_used = data.get("context_used", [])
                    
                    st.markdown(answer)
                    if context_used:
                        with st.expander("View Source Citations"):
                            for idx, ctx in enumerate(context_used):
                                st.markdown(f"**Chunk {idx+1}** (Distance: {ctx.get('distance', 'N/A')}):")
                                st.text(ctx.get('text', ''))
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": answer,
                        "context": context_used
                    })
                else:
                    err = res.json().get("error", "Unknown Error")
                    st.error(f"Backend Error: {err}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
