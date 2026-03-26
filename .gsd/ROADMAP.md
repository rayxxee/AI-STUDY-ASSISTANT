# ROADMAP.md

> **Current Phase**: Not started
> **Milestone**: v1.0

## Must-Haves (from SPEC)
- [ ] Users can upload documents (PDF, DOCX, TXT) and system extracts text.
- [ ] System generates vector embeddings and stores in FAISS.
- [ ] User can ask queries and receive context-aware answers using Gemini.
- [ ] Responses seamlessly include precise source citations.
- [ ] Built-in Chat memory manages recent messages.
- [ ] Basic Streamlit UI for interaction.

## Phases

### Phase 1: Foundation (Data Ingestion & Vector Store)
**Status**: ✅ Complete
**Objective**: Setup Flask, handle document uploads, extract text, chunk, and embed into FAISS.
**Requirements**: REQ-01 (partial), REQ-03, REQ-04, REQ-05

### Phase 2: Core RAG & LLM Integration
**Status**: ✅ Complete
**Objective**: Implement retrieval from FAISS and Gemini LLM generation with context mapping.
**Requirements**: REQ-01 (partial), REQ-06, REQ-07, REQ-10 (Citations)

### Phase 3: Memory & Advanced Features
**Status**: ✅ Complete
**Objective**: Add chat history, basic text summarization, query rewriting, and multi-doc reasoning handling.
**Requirements**: REQ-08, REQ-09, REQ-11, REQ-12, REQ-14

### Phase 4: Streamlit UI Integration
**Status**: ✅ Complete
**Objective**: Build Streamlit UI connecting to the Flask backend effectively.
**Requirements**: REQ-02

### Phase 5: Testing & Deployment Prep
**Status**: ✅ Complete
**Objective**: Integrate agent tools (PDF search tool) and Dockerize the entire system.
**Requirements**: REQ-13, REQ-15
