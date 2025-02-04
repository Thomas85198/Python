import re

text = "my phone number is 08-7555555, and 07-4147744"
print(re.findall(r"0\d-\d{7}", text))  # ['08-7555555', '07-4147744']

text = "This island is beautiful isn't it"
print(re.findall(r"\bis\b", text))  # ['is']

text = "Are you a dog person or a cat person"
print(re.findall(r"dog|cat", text))  # ['dog', 'cat']
