from collections import Counter

# my_list = [1, 2, 2, 3, 3, 3, 1, 1, 3, 2, 2, 3]

# result = Counter(my_list)
# print(result)  # Counter({3: 5, 2: 4, 1: 3})

# letters = "aaaaabbbbbcccccdddd"
# result = Counter(letters)
# print(result)  # Counter({'a': 5, 'b': 4, 'c': 5, 'd': 4})
# print(result.most_common(1))  # [('a', 5)]

from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", ["x", "y"])

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_length = sqrt((pt1.x-pt2.x) ** 2 + (pt1.y-pt2.y) ** 2)
print(line_length)

# factory function
# def default_factory():
#     return "This is not defined."


# d = defaultdict(default_factory)
# d["a"] = 1
# d["b"] = 2

# print(d["a"], d["b"], d["c"])

# Harry = defaultdict(lambda: "Wrong key")
# Harry["name"] = "Harry"
# Harry["age"] = 15

# print(Harry["name"], Harry["age"], Harry["school"])
