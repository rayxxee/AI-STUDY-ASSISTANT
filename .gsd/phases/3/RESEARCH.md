# Phase 3 Research: Memory & Advanced Features

## Decisions Made

1. **Memory System**: A simple rolling window in-memory dictionary or list in `memory/chat_memory.py`. It will hold the last 5 Q&A pairs to feed into generation, avoiding context window explosions.
2. **Query Rewriting**: LLMs struggle with semantic retrieval when queries contain pronouns ("What does it mean?"). `rag/rewriter.py` will hit Gemini *first* to rewrite vague queries utilizing the `chat_memory`, then pass the explicit query to FAISS.
3. **Summarization**: A new endpoint `/summarize` will be built to aggregate text from the vector knowledge base to yield document-level holistic summaries.
