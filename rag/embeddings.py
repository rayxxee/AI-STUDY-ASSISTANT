import os
import google.generativeai as genai

def get_embeddings(text_chunks, api_key=None):
    """
    Call Gemini Embedding API and return a list of numerical vectors.
    Uses 'models/embedding-001' which outputs 768-dimensional floats.
    """
    # Prefer passed api_key, fallback to env variable
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is not set.")
        
    genai.configure(api_key=key)
    
    embeddings = []
    # Gemini usually expects text-embedding-004 but embedding-001 is common as well.
    # We will use text-embedding-004 to be up to date if it exists, fallback to standard.
    # The SDK handles batch embedding if wrapped correctly, but we'll do iterative for safety on limits.
    for chunk in text_chunks:
        response = genai.embed_content(
            model="models/gemini-embedding-001",
            content=chunk,
            task_type="retrieval_document",
        )
        embeddings.append(response['embedding'])
        
    return embeddings
