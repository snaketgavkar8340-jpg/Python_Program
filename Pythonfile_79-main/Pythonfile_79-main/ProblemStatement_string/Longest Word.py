s = input("Enter a sentence: ")
words = s.split()

if words:
    print("Longest word:", max(words, key=len))