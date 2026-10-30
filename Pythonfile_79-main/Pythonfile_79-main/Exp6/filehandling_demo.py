# Create and write a file
f = open("sample.txt", "w")
f.write("Welcome to Python Programming")
f.close()

# Read the file
f = open("sample.txt", "r")
print("File Content:", f.read())
f.close()

# Append data
f = open("sample.txt", "a")
f.write("\nFile handling example")
f.close()

print("Data written successfully")