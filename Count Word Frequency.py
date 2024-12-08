from collections import Counter

text = input("Enter a text: ").lower()
words = text.split()
word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")
