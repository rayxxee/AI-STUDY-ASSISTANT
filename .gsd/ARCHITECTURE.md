# ARCHITECTURE.md - System Architecture

## Overview
The AI Study Assistant is designed as a RAG (Retrieval-Augmented Generation) system utilizing a Flask backend and a Streamlit frontend UI. The system aims to process personal study documents, maintain stateful conversational memory, and generate contextually accurate answers using Gemini APIs.

## 1. Data Ingestion Layer
- **Input Types**: PDFs, DOCX, TXT files
- **Tooling**: `PyMuPDF` or `pdfplumber` for structured text extraction
- **Output**: Cleaned and preprocessed raw text chunks ready for vectorization

## 2. Chunking & Embeddings
- **Strategy**: 300-500 tokens per chunk with sliding window overlap
- **Tooling**: Gemini Embeddings API

## 3. Vector Database
- **Tooling**: `FAISS`
- **Purpose**: Fast similarity check and Top-K chunk retrieval based on user query embeddings

## 4. Retrieval System
- Converts queries sequentially to embeddings -> Queries FAISS -> Returns top-K matched context chunks

## 5. LLM Generation Layer
- **Tooling**: Gemini Generative AI models
- **Input**: User query + Top-K contexts
- **Goal**: Formulate accurate context-aware responses with mandatory Source Citation

## 6. Memory & State Management
- **Short-Term Memory**: Sliding window of the last N conversation turns
- **Long-Term Memory**: Extracted summarizations and subject-based organization
- **Feature**: Subject-based segregation (e.g. AI notes vs Math notes)

## 7. API / Backend (Flask)
- `POST /upload`: Handles document uploads and indexing triggers
- `POST /query`: Handles chat queries and Generation pipeline
- `GET /history`: Returns chat and interaction history

## 8. Agent Tool Use
- PDF search integration
- Re-writing vague queries before hitting the main generation pipeline
- Calculator integration capabilities (Future scope/Optional)
- Smart summarizations

## 9. Frontend Layer (Streamlit)
- Rapid prototyping UI containing: File upload mechanism, subject selectors, and chat interface history layout

## 10. Deployment Strategy
- **Containerization**: Target fully containerized Docker architecture encapsulating Flask API + Vector Store + UI layers if feasible.

## Project Structure Map
```text
ai-study-assistant/
│
├── app.py                      # Main Flask application entrypoint
├── streamlit_app.py            # Streamlit UI implementation
├── routes/
│   ├── upload.py
│   ├── query.py
│
├── rag/
│   ├── retriever.py
│   ├── embeddings.py
│   ├── vector_store.py
│
├── memory/
│   ├── chat_memory.py
│
├── utils/
│   ├── text_processing.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```
