# ==========================================
# AI PIPELINE
# ==========================================

from src.retrieval import get_top_matches
from src.generator import generate_answer


def ask_ai(question):

    retrieved = get_top_matches(
        question,
        top_k=3
    )

    answer = generate_answer(
        question,
        retrieved
    )

    confidence = round(
        retrieved[0]["score"] * 100,
        2
    )

    return {
        "answer": answer,
        "retrieved": retrieved,
        "confidence": confidence
    }