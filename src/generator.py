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

    prompt = f"""
You are a professional sexual health information assistant.

Answer ONLY using the information below.

Question:
{question}

Relevant Information:
{context}

Provide a clear, concise, medically responsible answer.

Answer:
"""

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

        do_sample=False
    )

    answer = tokenizer.decode(

        outputs[0],

        skip_special_tokens=True
    )

    return answer