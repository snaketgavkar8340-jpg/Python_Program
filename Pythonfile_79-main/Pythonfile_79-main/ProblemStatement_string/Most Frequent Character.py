s = input("Enter a string: ")

if s:
    ch = max(dict.fromkeys(s), key=s.count)
    print("Most frequent:", ch)