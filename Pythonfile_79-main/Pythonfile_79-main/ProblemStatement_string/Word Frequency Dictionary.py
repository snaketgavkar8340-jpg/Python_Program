s = input("Enter a paragraph: ").lower().split()
freq = {}

for word in s:
    freq[word] = freq.get(word, 0) + 1

print(freq)