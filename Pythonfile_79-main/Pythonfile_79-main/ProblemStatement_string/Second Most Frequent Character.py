s = input("Enter a string: ")
freq = sorted(set(s), key=s.count, reverse=True)

if len(freq) >= 2:
    print("Second most frequent:", freq[1])
else:
    print("Not enough distinct characters")