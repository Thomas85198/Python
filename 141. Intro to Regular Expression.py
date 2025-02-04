import re

text = "from, My number is 0911111113. I am avaliable from 8am to 5pm, fromi"

patt = "from"

match = re.findall(patt, text)
print(re.search(patt, text))  # <re.Match object; span=(40, 44), match='from'>
# print(match.group())
# print(match.start())
# print(match.span())
# print(match.end())

print(match)  # ['from', 'from', 'from']
