import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Global variables for lazy loading
_model = None
_df = None
_question_embeddings = None

def get_top_matches(query: str, top_k: int = 3):
    global _model, _df, _question_embeddings
    
    # Lazy load to avoid overhead when importing
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    if _df is None:
        _df = pd.read_pickle(os.path.join(MODEL_DIR, "knowledge_base.pkl"))
    if _question_embeddings is None:
        _question_embeddings = np.load(os.path.join(MODEL_DIR, "question_embeddings.npy"))
        
    # Embed the query
    query_embedding = _model.encode(query, convert_to_numpy=True)
    
    # Compute cosine similarity
    norms = np.linalg.norm(_question_embeddings, axis=1)
    query_norm = np.linalg.norm(query_embedding)
    
    # Handle division by zero just in case
    norms[norms == 0] = 1e-9
    if query_norm == 0:
        query_norm = 1e-9
        
    similarities = np.dot(_question_embeddings, query_embedding) / (norms * query_norm)
    
    # Get indices of the highest similarity scores
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({
            "score": float(similarities[idx]),
            "question": _df.iloc[idx]["input"],
            "answer": _df.iloc[idx]["output"]
        })
        
    return results
