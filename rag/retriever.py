from rag.embeddings import get_embeddings

def retrieve_context(query, vector_store, top_k=3):
    """
    Takes a string query, computes its embedding, and fetches
    the top-K closest matching text chunks from the vector store.
    """
    if not query.strip():
        return []
        
    try:
        # get_embeddings expects a list of texts
        query_embedding = get_embeddings([query])[0]
        results = vector_store.search_similar(query_embedding, top_k=top_k)
        return results
    except Exception as e:
        print(f"Retrieval error: {e}")
        return []
