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

    # Convert the user question into an embedding
    user_embedding = embedding_model.encode(
        [user_question],
        convert_to_numpy=True
    ).astype("float32")

    # Normalize for cosine similarity
    faiss.normalize_L2(user_embedding)

    # Search the FAISS index
    scores, indices = index.search(
        user_embedding,
        top_k * 3   # Retrieve extra results to remove duplicates
    )

    results = []
    seen_questions = set()

    for score, idx in zip(scores[0], indices[0]):

        question = knowledge_base.iloc[idx]["input"]

        # Skip duplicate questions
        if question in seen_questions:
            continue

        seen_questions.add(question)

        results.append({
            "question": question,
            "answer": knowledge_base.iloc[idx]["output"],
            "score": float(score)
        })

        # Stop once we have enough unique results
        if len(results) == top_k:
            break

    return results