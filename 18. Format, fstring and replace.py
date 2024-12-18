name = "Josh Jordan"
print(name.replace("J", "K"))  # Kosh Kordan

sentence = "Today is a good day."
print(sentence.split(" "))  # ['Today', 'is', 'a', 'good', 'day.']
# ['T', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'o', 'o', 'd', ' ', 'd', 'a', 'y', '.']
print(list(sentence))

# string, number, boolean, dict, set, tuple, list
# format(), fstring
print("I have a string {}".format(15))  # I have a string 15
# I have a string ['asdkf', 'kasjdfk']
print("I have a string {}".format(["asdkf", "kasjdfk"]))
# 20, here is another string, 3.14
print("{}, {}, {}".format(20, "here is another string", 3.14))
print("{0}, {0}, {0}".format(20, "here is another string", 3.14))  # 20, 20, 20
print("{name}, {address}, {age}".format(name="Wilson", age=20,
      height=5.8, address="Hawaii"))


myName = "Thomas"
age = 30

# Hello,km my name is Thomas, I am 30 years old.
print(f"Hello,km my name is {myName}, I am {age} years old.")
