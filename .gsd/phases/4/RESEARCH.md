# Phase 4 Research: Streamlit UI Integration

## Decisions Made

1. **Framework**: Streamlit is perfect for rapid AI prototyping. It drastically reduces HTML/JS writing requirements while offering native chat components.
2. **Architecture**: The UI runs as a separate process (`streamlit run ui/app.py`) from the Flask backend. It will use the standard `requests` library to communicate HTTP payloads to `http://localhost:5000/`.
3. **State Management**: `st.session_state` tracks the visual chat blobs on the frontend for rendering, while the backend independently maintains the true memory buffer to feed the LLM.
