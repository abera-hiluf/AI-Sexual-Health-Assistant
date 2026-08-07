# ==========================================
# RETRIEVAL MODULE (FAISS VERSION)
# ==========================================

import os
import streamlit as st

# ------------------------------------------
# Paths
# ------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

@st.cache_resource(show_spinner=False)
def _load_retrieval_resources():
    """Load retrieval resources once per running Streamlit process."""
    import faiss
    import pandas as pd
    # pyrefly: ignore [missing-import]
    from sentence_transformers import SentenceTransformer

    print("Loading embedding model and knowledge base...")

    embedding_model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    index = faiss.read_index(
        os.path.join(MODEL_DIR, "health_index.faiss")
    )
    knowledge_base = pd.read_pickle(
        os.path.join(MODEL_DIR, "knowledge_base.pkl")
    )

    print("Retrieval resources loaded.")
    return embedding_model, index, knowledge_base

# ------------------------------------------
# Retrieval Function
# ------------------------------------------

def get_top_matches(user_question, top_k=3):

    import faiss

    embedding_model, index, knowledge_base = _load_retrieval_resources()

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
