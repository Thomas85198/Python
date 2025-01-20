# import __builtins__ # __builtins__ module is alson an object
# print(__builtins__)

x = "This is a string."

print(__builtins__.len(x))  # Output: 16
print(dir(__builtins__))


print(globals())  # return global namespace as a dictionary
