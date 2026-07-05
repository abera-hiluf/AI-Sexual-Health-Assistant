# ==========================================
# CREATE FAISS INDEX
# ==========================================

import os
import faiss
import numpy as np

print("=" * 50)
print("Creating FAISS Index...")
print("=" * 50)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "models")

embedding_path = os.path.join(
    MODEL_DIR,
    "question_embeddings.npy"
)

embeddings = np.load(embedding_path)

embeddings = embeddings.astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

faiss.normalize_L2(embeddings)

index.add(embeddings)

faiss.write_index(
    index,
    os.path.join(MODEL_DIR, "health_index.faiss")
)

print("FAISS Index created successfully!")

print(f"Total vectors: {index.ntotal}")