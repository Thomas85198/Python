# def cube(n):
#     result = []
#     for x in range(n):
#         result.append(n ** 3)
#     return result

# for i in cube(10):
#     print(i)
#     for x in range(n):
#         yield x ** 3


# print(cube(10))

# for element in cube(10):
#     print(element)

def sub_generator(x):
    for i in range(x):
        yield i ** 2


def gen(y):
    yield from sub_generator(y)


for num in gen(15):
    print(num)
