# lambda variable: operation
result = (lambda x: x**2)(5)
print(result)

# lambda input1, input2, ...: operation
myTuple = (lambda x, y: (x + y, x - y))(15, 30)
print(myTuple[0])
print(myTuple[1])

# map
for item in map(lambda x: x**2, [15, 10, 5, 0]):
    print(item)

# filter
for item in filter(lambda x: x % 2 == 0, [15, 10, 5, 0]):
    print(item)
