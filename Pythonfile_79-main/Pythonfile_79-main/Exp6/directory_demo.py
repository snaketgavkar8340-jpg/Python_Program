import os

# Create a directory
os.makedirs("MyFolder", exist_ok=True)
print("Directory created")

# Display current directory
print("Current Directory:", os.getcwd())

# List files and directories
print("Contents:", os.listdir("."))

# Remove the directory if it is empty
os.rmdir("MyFolder")
print("Directory removed")