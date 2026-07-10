# ==========================================
# AI PIPELINE
# ==========================================

from src.retrieval import get_top_matches
from src.generator import generate_answer


def ask_ai(question, confidence_threshold=0.45, top_k=3):

    retrieved = get_top_matches(
        question,
        top_k=top_k
    )

    if not retrieved or retrieved[0]["score"] < confidence_threshold:
        confidence = round(retrieved[0]["score"] * 100, 2) if retrieved else 0.0
        return {
            "answer": "I am sorry, but your question does not seem to be related to the sexual health topics covered in my knowledge base (such as HIV, STIs, testing, prevention, or treatment). Please ask a sexual health-related question, or consult a healthcare professional for specific medical advice.",
            "retrieved": [],
            "confidence": confidence,
            "is_related": False
        }

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
        "confidence": confidence,
        "is_related": True
    }