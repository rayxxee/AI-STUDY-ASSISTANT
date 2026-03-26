import os
import faiss
import numpy as np
import pickle

class VectorStore:
    def __init__(self, index_path=".gsd/faiss_index.bin", metadata_path=".gsd/faiss_metadata.pkl", dim=768):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.dim = dim
        self.texts = []
        
        if os.path.exists(self.index_path) and os.path.exists(self.metadata_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, 'rb') as f:
                self.texts = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dim)
            
    def add_texts(self, chunks, embeddings):
        if not chunks or not embeddings:
            return
            
        embeddings_np = np.array(embeddings).astype('float32')
        self.index.add(embeddings_np)
        self.texts.extend(chunks)
        self.save()
        
    def search_similar(self, query_embedding, top_k=3):
        if self.index.ntotal == 0:
            return []
            
        query_np = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_np, top_k)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1 and idx < len(self.texts):
                results.append({
                    "text": self.texts[idx],
                    "distance": float(distances[0][i])
                })
        return results
        
    def save(self):
        # Ensure directories exist
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, 'wb') as f:
            pickle.dump(self.texts, f)
