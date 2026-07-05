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

    return {

        "answer": answer,

        "retrieved": retrieved

    }
