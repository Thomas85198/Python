# def sum(*args):
#     # print(args)
#     # print(type(args))
#     # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     # <class 'tuple'>
#     result = 0
#     for number in range(0, len(args)):
#         result += args[number]
#         print(f"Now, the result is {result}")
#     return result


# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def myfunc(**kwargs):
#     print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


# myfunc(name="Wilson", age=25, address="Hawaii")
def myfunc(*args, **kwargs):
    print("I would like to eat {} {}".format(args[2], kwargs["food"]))


myfunc(14, 17, 23, "Hello", name="Wilson", food="eggs")

# 1. normal argument (p1, p2)
# 2. default argument
# 3. *args
# 4. **kwargs


def func(p1, p2, p3="three", *args, **kwargs):
    print("--------------------")
    print(p1, p2, p3, args, kwargs)


func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, x=4)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)
