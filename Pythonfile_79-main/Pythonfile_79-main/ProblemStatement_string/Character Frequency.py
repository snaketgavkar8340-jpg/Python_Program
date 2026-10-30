s = input("Enter a string: ")

for ch in dict.fromkeys(s):
    print(ch, ":", s.count(ch))