def exponent(a, b):
    return a ** b


# positional arguments
print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9

# keyword arguments
print(exponent(a=10, b=2))  # 100
print(exponent(b=2, a=10))  # 100

myList = [4, 6, 3, 2, 1]
print(sorted(myList))  # [1, 2, 3, 4, 6]
