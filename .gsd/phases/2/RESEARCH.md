# Phase 2 Research: Core RAG & LLM Integration

## Decisions Made

1. **Retriever Logic**: Isolated in `rag/retriever.py` to keep context lookup logic decoupled from generation.
2. **LLM Generation**: Google's `gemini-1.5-flash` via `google-generativeai` SDK. Highly capable, fast, and cost-effective. Given the requirement for citations, strict RAG prompting principles will be used instructing the model to rely solely on the provided context block and cite it.
3. **Routing**: `routes/query.py` acts as the primary orchestrator wrapping `Retrieval -> Generation` under the `/query` endpoint.
