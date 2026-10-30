email = input("Enter email: ")
parts = email.split("@")

if (len(parts) == 2 and parts[0] and
    "." in parts[1] and
    not parts[1].startswith(".") and
    not parts[1].endswith(".")):
    print("Valid format")
else:
    print("Invalid format")