import shelve

# integers1 = [1, 2, 3, 4, 5, 6]
# integers2 = [6, 7, 8, 9, 10]
# integers3 = [100, 101, 102, 103]

# with shelve.open("shelf-example", 'c') as shelf:
#     shelf['ints1'] = integers1
#     shelf['ints2'] = integers2
#     shelf['ints3'] = integers3


with shelve.open("shelf-example", 'r') as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf['ints2'])
