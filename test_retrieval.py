from src.retrieval import get_top_matches

results = get_top_matches(
    "Can HIV be cured?"
)

for i, result in enumerate(results, 1):

    print(f"\nMATCH {i}")

    print(result["score"])

    print(result["question"])

    print(result["answer"])