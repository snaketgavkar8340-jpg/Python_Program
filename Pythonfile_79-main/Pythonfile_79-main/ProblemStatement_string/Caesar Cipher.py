s = input("Enter a message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - base + shift) % 26 + base)
    else:
        result += ch

print("Encrypted:", result)