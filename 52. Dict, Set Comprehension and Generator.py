x = [1, 2, 3, 4]

# x_squared_dict = {item: item ** 2 for item in x}

# print(x_squared_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}

# x_squared_set = {item ** 2 for item in x if item > 2}

# print(x_squared_set)  # {16, 9}

x_squared_generator = (item ** 2 for item in x)

# <generator object <genexpr> at 0x0000020D3D3D3F90>
print(x_squared_generator)

for i in x_squared_generator:
    print(i)
