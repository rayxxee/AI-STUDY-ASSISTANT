# REQUIREMENTS.md

## Format
| ID | Requirement | Source | Status |
|----|-------------|--------|--------|
| REQ-01 | Build Flask backend containing `/upload`, `/query`, and `/history` endpoints | Architecture 7 | Pending |
| REQ-02 | Build a Streamlit UI for chat, document upload, and history view | Architecture UI | Pending |
| REQ-03 | Extract text from uploaded PDF/DOCX/TXT using PyMuPDF/pdfplumber | Architecture 1 | Pending |
| REQ-04 | Chunk extracted text into 300–500 token sizes and generate embeddings via Gemini | Architecture 2 | Pending |
| REQ-05 | Initialize and store vector embeddings in FAISS vector database | Architecture 3 | Pending |
| REQ-06 | Implement Retrieval System to fetch top-k document chunks based on semantic similarity | Architecture 4 | Pending |
| REQ-07 | Implement Gemini LLM Generation Layer mapping retrieved context and user query | Architecture 5 | Pending |
| REQ-08 | Implement in-memory chat history and long-term memory for context context management | Architecture 6 | Pending |
| REQ-09 | Support Multi-Document Reasoning across multiple data sources | Feature 1 | Pending |
| REQ-10 | Output precise source citations (e.g., "Page 5 of PDF") in LLM responses | Feature 2 | Pending |
| REQ-11 | Provide smart summarization capability for entire documents | Feature 3 | Pending |
| REQ-12 | Implement Advanced Query Rewriting to clarify vague queries | Feature 4 | Pending |
| REQ-13 | Integrate Agent Tool Use (PDF search, optional Calculator/Web search) for dynamic reasoning | Feature 5 | Pending |
| REQ-14 | Implement Subject-Based Memory routing to organize notes logically | Feature 6 | Pending |
| REQ-15 | Dockerize entire application structure using `Dockerfile` | Architecture 8 | Pending |
