x = [1, 2, 3, 4]
# squared_x = []
# for item in x:
#     squared_x.append(item ** 2)


squared_x = [item ** 2 for item in x if item >= 3]
print(squared_x)
