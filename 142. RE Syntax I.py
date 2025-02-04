import re

# regular expression => raw string
print(r"\n")  # \n

text = "hello, heabo, hecdo, he56o"
print(re.findall(r"he[abcl][a-d]o", text))  # ['heabo', 'hecdo']

text = "How are you doing today?"
print(re.findall(r"[a-d]", text))  # ['a', 'd', 'd', 'a']

text = "hello, heabo, hecdo, he56o, hellooo"
# ['hello', 'heabo', 'hecdo', 'he56o', 'hello']
print(re.findall(r"he..o", text))

text = "hello, heo, helllllo, hekko"
print(re.findall(r"he.*o", text))  # ['hello, heo, helllllo, hekko']

text = "I say hello6, hello747 and, hello696"
print(re.findall(r"hello\d{1,3}", text))  # ['hello6', 'hello747', 'hello696']
