# Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.
# def printMany():
#     for i in range(1, 101):
#         print(i)


# printMany()

# Write a function called printEvery3 that prints out integers 1, 4, 7, 10, ..., 88.
# def printEvery3():
#     for i in range(1, 89, 3):
#         print(i)


# printEvery3()

# Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.
# def position(string):
#     for counter, char in enumerate(string):
#         if char.upper() == char:
#             return char, counter
#         else:
#             return -1


# result = position("abcd")
# result1 = position("AbcD")
# result2 = position("abCD")
# print(result)
# print(result1)
# print(result2)

# Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.

def findSmallCount(lst, targetNum):
    count = 0
    for i in filter(lambda x: x < targetNum, lst):
        count += 1
    return count


print(findSmallCount([1, 2, 3], 2))
print(findSmallCount([1, 2, 3, 4, 5], 0))
