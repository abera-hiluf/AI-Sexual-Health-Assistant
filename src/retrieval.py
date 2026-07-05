# ==========================================
# RETRIEVAL MODULE (FAISS VERSION)
# ==========================================

import os
import faiss
import numpy as np
import pandas as pd
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

# ------------------------------------------
# Paths
# ------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "models")

# ------------------------------------------
# Load MiniLM
# ------------------------------------------

print("Loading embedding model...")

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded.")

# ------------------------------------------
# Load FAISS Index
# ------------------------------------------

index = faiss.read_index(
    os.path.join(MODEL_DIR, "health_index.faiss")
)

knowledge_base = pd.read_pickle(
    os.path.join(MODEL_DIR, "knowledge_base.pkl")
)

print("Knowledge base loaded.")

# ------------------------------------------
# Retrieval Function
# ------------------------------------------

def get_top_matches(user_question, top_k=3):

    user_embedding = embedding_model.encode(
        [user_question],
        convert_to_numpy=True
    ).astype("float32")

    faiss.normalize_L2(user_embedding)

    scores, indices = index.search(
        user_embedding,
        top_k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        results.append({

            "question": knowledge_base.iloc[idx]["input"],

            "answer": knowledge_base.iloc[idx]["output"],

            "score": float(score)

        })

    return results