import datetime

print(datetime.datetime.now())
print(type(datetime.datetime.now()))

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

y = datetime.datetime(2022, 5, 1)
print(x.strftime("%Y"))
print(x - y)
