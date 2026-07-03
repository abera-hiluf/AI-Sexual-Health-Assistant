# ==========================================
# CREATE EMBEDDINGS FOR KNOWLEDGE BASE
# ==========================================

import os
import numpy as np
import pandas as pd
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer


print("=" * 50)
print("Loading dataset...")
print("=" * 50)

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data path
DATA_PATH = os.path.join(BASE_DIR, "data", "english_train.csv")

# Output path
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded successfully!")
print(f"Total Questions: {len(df)}")

print("\nLoading MiniLM model...")

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model loaded successfully!")

print("\nCreating embeddings...")

questions = df["input"].tolist()

question_embeddings = embedding_model.encode(
    questions,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("\nSaving embeddings...")

np.save(
    os.path.join(MODEL_DIR, "question_embeddings.npy"),
    question_embeddings
)

print("Embeddings saved!")

print("\nSaving knowledge base...")

df.to_pickle(
    os.path.join(MODEL_DIR, "knowledge_base.pkl")
)

print("Knowledge base saved!")

print("\nDone!")
print("=" * 50)
