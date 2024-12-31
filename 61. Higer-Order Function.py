# def higherOrder(fn):
#     fn()


# def smallfunc():
#     print("Hello from small function.")


# higherOrder(smallfunc)

# def square(num):
#     return num ** 2


# myList = [-10, 3, 9, 8, 10]
# print(map(square, myList))

# for item in map(square, myList):
#     print(item)

def even(num):
    return num % 2 == 0


myList = [444532, 3211543, -998432, 66154]
for item in filter(even, myList):
    print(item)
