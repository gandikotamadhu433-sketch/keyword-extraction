print("========================================")
print("        KEYWORD EXTRACTOR")
print("========================================")

text = input("\nEnter your text:\n")

stop_words = [
    "the", "is", "a", "an", "and", "or",
    "of", "to", "in", "on", "for", "with",
    "this", "that", "are", "was", "were",
    "it", "as", "by", "from"
]

words = text.lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")

    if word not in stop_words and len(word) > 2:
        frequency[word] = frequency.get(word, 0) + 1

keywords = sorted(
    frequency,
    key=frequency.get,
    reverse=True
)

print("\n----------------------------------------")
print("IMPORTANT KEYWORDS:")
print("----------------------------------------")

for word in keywords[:10]:
    print(word, "->", frequency[word], "time(s)")

print("----------------------------------------")