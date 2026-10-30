s = input("Enter a sentence: ")
words = s.split()

if words:
    print("Shortest word:", min(words, key=len))