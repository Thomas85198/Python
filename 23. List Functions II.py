friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
my_lost_friend = friends.pop()
print(friends)  # ["Wilson", "Mike", "Nelson", "Greg"]
print(my_lost_friend)  # Jimmy


x = [1, 2, 3, 4, 5, 6]
y = x
y[0] = 15
print(x)  # [15, 2, 3, 4, 5, 6]
print(y)  # [15, 2, 3, 4, 5, 6]

print("-------------------------")
a = 10
b = a
b = 15
print(a)  # 10
print(b)  # 15

print("-------------------------")
x = [1, 2, 3, 4, 5, 6]
y = x.copy()
y[0] = 15
print(x)  # [1, 2, 3, 4, 5, 6]
print(y)  # [15, 2, 3, 4, 5, 6]
