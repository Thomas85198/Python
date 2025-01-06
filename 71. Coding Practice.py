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

# def findSmallCount(lst, targetNum):
#     count = 0
#     for i in filter(lambda x: x < targetNum, lst):
#         count += 1
#     return count


# print(findSmallCount([1, 2, 3], 2))
# print(findSmallCount([1, 2, 3, 4, 5], 0))

# Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, and returns the sum of all elements in the list that are smaller than the input integer.
# def findSmallerTotal(lst, targetNum):
#     sum = 0
#     for i in filter(lambda x: x < targetNum, lst):
#         sum += i
#     return sum


# print(findSmallerTotal([1, 2, 3], 3))
# print(findSmallerTotal([1, 2, 3], 1))
# print(findSmallerTotal([3, 2, 5, 8, 7], 999))
# print(findSmallerTotal([3, 2, 5, 8, 7], 0))

# Write a function called "findAllSmall" that takes one list of integers and another integer as input, and returns an list of integers that contains all elements that are smaller than the input integer.
# def findAllSmall(lst, targetNum):
#     result = []
#     for i in filter(lambda x: x < targetNum, lst):
#         result.append(i)
#     return result


# print(findAllSmall([1, 2, 3], 10))
# print(findAllSmall([1, 2, 3], 2))
# print(findAllSmall([1, 3, 5, 4, 2], 4))

# Write a function called "summ" that takes one list of numbers, and return the sum of all elements in the input list.
# def summ(lst):
#     sum = 0
#     if (len(lst) == 0):
#         sum = 0
#         return sum
#     for i in lst:
#         sum += i
#     return sum


# print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
# print(summ([]))  # return 0
# print(summ([-10, -20, -30]))  # return -60

# Write a function called "stars" which prints out layers of stars in the following pattern:
# def stars(num):
#     for i in range(1, num + 1):
#         print("*" * i)

# stars(1)
# stars(4)

# Write a function called "stars2" which prints out layers of stars in the following pattern:
# def stars2(num):
#     for i in range(1, num + 1):
#         print("*" * i)
#     for i in range(num - 1, 0, -1):
#         print("*" * i)


# stars2(1)
# stars2(2)
# stars2(3)
# stars2(4)

# Write a function called "table" which takes an input n, and prints out n x 1 to n x 9
# def table(num):
#     for i in range(1, 10):
#         print(f"{num} x {i} = {num * i}")

# table(3)

# Write a function called "table9to9" that prints out the multiplication table:
# def table9to9():
#     for i in range(1, 10):
#         for j in range(1, 10):
#             print(f"{i} x {j} = {i * j}")


# table9to9()

# Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase, uppercase changed to lowercase.
# def swap(str):
#     result = ""
#     if (len(str) == 0):
#         return result
#     for item in str:
#         if item.isupper():
#             result += item.lower()
#         elif item.islower():
#             result += item.upper()
#         elif item.isspace():
#             result += item
#         else:
#             result += item
#     return result


# print(swap("Aloha"))
# print(swap("Love you."))

# Write a function called "findMin" which takes an list as input, and returns the minimum element in the input list.
# def findMin(lst):
#     if (len(lst) == 0):
#         print("undefined")
#         return
#     result = min(lst)
#     print(result)


# findMin([1, 2, 5, 6, 99, 4, 5])  # returns 1
# findMin([])  # returns undefined
# findMin([1, 6, 0, 33, 44, 88, -10])  # returns -10

# Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.
# def mySort(lst):
#     if (len(lst) == 0):
#         return []

#     for i in range(len(lst)):
#         min = i
#         for j in range(i + 1, len(lst)):
#             if lst[j] < lst[min]:
#                 lst[j], lst[min] = lst[min], lst[j]
#     return lst

# print(mySort([17, 0, -3, 2, 1, 0.5]))

# Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
# def isPrime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# print(isPrime(1))
# print(isPrime(5))
# print(isPrime(91))
# print(isPrime(1000000))

# Write a function called "palindrome" that checks if the input string is a palindrome. (Search on google if you don't know what a palindrome is.)
# def palindrome(str):
#     if str == str[::-1]:
#         return True
#     return False


# print(palindrome("bearaeb"))  # true
# print(palindrome("Whatever revetahW"))  # true
# print(palindrome("Aloha, how are you today?"))  # false

# Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:
def pyramid(num):
    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))


# pyramid(1)
# pyramid(2)

# Write a function called "inversePyramid" that draws pyramid upside down.


# def inversePyramid(num):
#     for i in range(num, 0, -1):
#         print(" " * (num - i) + "*" * (2 * i - 1))


# inversePyramid(4)

# Given a list of ints, return True if the list contains a 3 next to a 3.
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 5, 7, 3, 3]))  # True
print(has_33([]))  # False
print(has_33([4, 3, 2, 1, 0]))  # False

# Write a function that check if a list contains a subsequence of 007


# def spyGame(lst):
#     code = [0, 0, 7]
#     for num in lst:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 0


# print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
# print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False

lst = [5, 2, 3, 4]

for i in range(len(lst)):
    print(lst[i])

for i in enumerate(lst):
    print(i)
