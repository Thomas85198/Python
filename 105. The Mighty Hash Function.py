a = 100
b = "This is just a string"
c = 1.0
d = True
e = None

# 100 2704644824836046309 1 1 4238894112
print(hash(a), hash(b), hash(c), hash(d), hash(e))
# TypeError: unhashable type: 'list'
# print(hash([1, 4, 7, 11]))
# dict 也不行，只有 set 可以
