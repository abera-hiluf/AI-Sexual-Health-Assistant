# ==========================================
# GENERATOR MODULE
# ==========================================

# pyrefly: ignore [missing-import]
import torch
# pyrefly: ignore [missing-import]
from transformers import AutoTokenizer
# pyrefly: ignore [missing-import]
from transformers import AutoModelForSeq2SeqLM

print("Loading FLAN-T5...")

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

generator_model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

# Use GPU if available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

generator_model.to(DEVICE)

print(f"Generator running on: {DEVICE}")

# ==========================================
# GENERATE ANSWER
# ==========================================

def generate_answer(
    question,
    retrieved_results
):

    context = "\n\n".join(
        [
            result["answer"]
            for result in retrieved_results
        ]
    )

    prompt = f"""You are an AI Sexual Health Information Assistant. Your purpose is to provide accurate, educational, and easy-to-understand sexual health information.

Rules:
1. Use ONLY the relevant information provided below to answer the question. Do not invent medical facts or use outside knowledge.
2. If the relevant information is insufficient to answer the question, state clearly that the retrieved information is insufficient.
3. Write in clear, supportive, and accessible language suitable for the general public.
4. Give practical recommendations when appropriate (e.g., getting tested, using protection).
5. Recommend consulting a healthcare professional for diagnosis, treatment, or emergencies.
6. Never claim certainty beyond the provided information.

Relevant Information:
{context}

Question:
{question}

Answer:"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to(DEVICE)

    outputs = generator_model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.3,
        do_sample=True
    )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer