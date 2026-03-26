import os
import google.generativeai as genai

def generate_answer(query, retrieved_contexts, chat_history_str=None, api_key=None):
    """
    Generates an answer from Gemini based ONLY on the provided contexts.
    Forces the model to include source citations.
    """
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        return "Error: GEMINI_API_KEY is not set."
        
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    if not retrieved_contexts:
        return "I couldn't find any relevant context in your uploaded documents to answer this question."
        
    context_block = ""
    for i, ctx in enumerate(retrieved_contexts):
        context_block += f"\n[Document Chunk {i+1}]:\n{ctx['text']}\n"
        
    history_block = ""
    if chat_history_str and chat_history_str != "No previous conversation.":
        history_block = f"Previous Conversation History:\n{chat_history_str}\n"

    prompt = f"""
You are an intelligent AI Study Assistant. Your task is to answer the user's question based strictly on the context provided below.

Rules:
1. If the context does not contain the answer, explicitly state that you don't know based on the provided documents. Do not hallucinate.
2. You MUST cite your sources by referencing the chunk number (e.g., "[Document Chunk 1]") whenever you state a fact from the text.

{history_block}Context:
{context_block}

User Question: {query}
Answer:
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with LLM: {str(e)}"
