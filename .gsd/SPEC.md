# SPEC.md — Project Specification

> **Status**: `FINALIZED`

## Vision
An intelligent RAG-based AI study assistant that acts as a personal tutor by ingesting personal study materials (PDFs, notes, slides), maintaining conversation memory, and providing context-aware, highly accurate answers using Gemini models.

## Goals
1. Enable flexible ingestion and textual extraction of user study materials (PDF, DOCX, TXT) using tools like PyMuPDF/pdfplumber.
2. Provide fast, semantic document retrieval using FAISS vector database and embeddings.
3. Generate accurate, context-aware answers using Gemini API with precise source citations ("Page 5 of PDF").
4. Maintain contextual conversation through advanced memory management (short-term chat history and long-term summaries).
5. Implement a robust backend using Flask and an intuitive, simple chat interface using Streamlit initially.

## Non-Goals (Out of Scope)
- Real-time collaborative document editing.
- Full-fledged enterprise user management and auth (for this initial version).
- Complex custom frontend architecture like React/Next.js (for this initial version).

## Users
Students, researchers, and self-learners who need to deeply understand their personal study materials, cross-reference multiple documents, and have an intelligent tutor that remembers context and cites its sources.

## Constraints
- **Technical**: Must be modularly organized (app.py, routes, rag, memory, utils), and deployable via Docker.
- **Model**: Dependent on Gemini API limits and capabilities. Vector DB must be FAISS.

## Success Criteria
- [ ] Architecture successfully decouples Flask backend and Streamlit frontend.
- [ ] Users can upload standard document types successfully.
- [ ] System accurately retrieves relevant context from multiple documents with low latency.
- [ ] Agent provides accurate answers accompanied by correct source citations.
- [ ] Reduced response hallucination by explicitly grounding answers in provided context.
- [ ] Agent remembers previous questions and notes (Subject-based memory and conversation history).
