# a = 30
# b = 25


# def addition(x, y):
#     print(x + y)


# addition(a, b)  # arguments can be variables as well
# 55

# global variables, local variables
# a = 5  # global variable


# def f1():
#     x = 2  # local variable
#     y = 3
#     print(x, y, a)


# def f2():
#     x = 10
#     y = 17
#     print(x, y, a)


# f1()

# parameters (inputs) are local variables in the function
a = 10
# a = [1, 2, 3, 4]


# def change(num):
#     # num = a (copy by value) => num = 10;
#     num = 25  # a = 25


# change(a)
# print(a)  # 10


# def change(list):
#     # list = a (copy by reference) => list = [1, 2, 3, 4]
#     list[0] = 100  # a = [100, 2, 3, 4]


# change(a)
# print(a)

# can we ever change any copy by value global variables?
# def change(num):
#     global a
#     a = 25


# change(a)
# print(a)

def myAddition(a, b):
    """This function docs addition of two numbers"""
    print(a + b)


help(myAddition)
