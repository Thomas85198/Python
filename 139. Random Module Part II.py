import random

random.seed(10)

for i in range(5):
    print(random.randint(1, 1000))

sentence = "Hi, this is just a sentence"

chosen_index = random.randrange(0, len(sentence))
print(chosen_index)
print(sentence[chosen_index])

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

random.shuffle(fruits)
print(fruits)
