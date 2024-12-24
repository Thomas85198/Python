x = 3 + 4j
y = 5 - 7j
print(x + y)


def hello():  # hello is stored in RAM
    print("hello")


print(hello)  # <function hello at 0x000001DC1925CA40>
print(hello())  # None

print(0.1 + 0.2 - 0.3)  # 5.551115123125783e-17 floating binary problem

myList = ["a", "b", "c", "d"]
myString = "|".join(myList)
print(myString)  # a|b|c|d
