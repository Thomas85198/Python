import os

print(os.getcwd())  # Get current working directory
# List all files and folders in current working directory
print(os.listdir(os.curdir))
print(os.pardir)


print(os.path.join("utils", "hello.html"))
