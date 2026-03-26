# Phase 1 Research: Data Ingestion & Vector Store

## Decisions Made

1. **Backend Framework**: Flask (`app.py`, `routes/`). Lightweight and perfect for a modular decoupling from Streamlit.
2. **Text Extraction**: `PyMuPDF` (`fitz`). Faster and highly robust for PDF parsing compared to alternatives like `pypdf2`. Python `docx` and built-in text reading handle the rest.
3. **Embeddings**: `google-generativeai`. Dimension size aligns with Gemini's text embedding model structure.
4. **Vector Store**: `faiss-cpu`. Simple, exceptionally fast, and allows local binary persistence without the overhead of spinning up a dedicated database container (like Qdrant or ChromaDB) for an initial MVP.
