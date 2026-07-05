from src.pipeline import ask_ai

question = "Can HIV be cured?"

result = ask_ai(question)

print("="*50)

print("ANSWER")

print("="*50)

print(result["answer"])

print("\n")

print("="*50)

print("SOURCES")

print("="*50)

for item in result["retrieved"]:

    print(item["score"])

    print(item["question"])

    print()