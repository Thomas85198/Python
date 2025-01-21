import something

try:
    num = 25
    something.enter_age(num)
except something.NegativeNumberException as error:
    print(error)
