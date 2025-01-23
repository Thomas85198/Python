# OOP obj # obj iterable, iterator
# iterable => (1) __iter__() method returns an iterator
# iterable => (2) implements __getitem__()
# any generator is an iterator by defult
# class Something:
#     def __iter__(self):
#         yield 5
#         for x in range(1, 4):
#             yield x


# s = Something()
# print(iter(s))
# for i in s:
#     print(i)

# class Building(object):
#     def __init__(self, floors):
#         self.__floors = [None] * floors

#     def __setitem__(self, floor_number, data):
#         self.__floors[floor_number] = data

#     def __getitem__(self, floor_number):
#         return self.__floors[floor_number]


# building1 = Building(4)
# building1[0] = 'Reception'
# building1[1] = 'ABC Corp'
# building1[2] = 'DEF Inc'

# for thing in building1:
#     print(thing)

# iterator is a subset of iterable
x = [1, 2, 3]
# print(dir(x))  # list is not iterator, iterable
# __iter__() returns a iterator

# print(dir(iter(x)))
# list_iterator = iter(x)

# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# for i in x:
#     print(i)

# self made iterator


class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.max_num:
            value = self.index
            self.index += 1
            return value
        else:
            self.index = 0
            raise StopIteration


my_iterator = MyIterator(5)
for item in my_iterator:
    print(item)
