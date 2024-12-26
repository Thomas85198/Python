# for variable in iterable:
#     do someting here

for letter in "Hello World":
    # print(letter.upper())
    if (letter == letter.upper()):
        print(letter)

myList = [1, 3, 5, 7, 9]

for num in myList:
    print(num ** 2)

# a list of tuples
for a, b in [(1, 2), (3, 5), (5, 7)]:
    print(a, b)
    print(tuple[0], tuple[1])

myDictionary = {"name": "Wilson", "age": 25}

for item in myDictionary.values():
    print(item)

for key, value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")

# set
for i in {1, 3, 5, 7, 9}:
    print(i)
