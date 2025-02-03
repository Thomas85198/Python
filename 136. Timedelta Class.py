import datetime

now = datetime.datetime.now()
oneday = datetime.datetime(2022, 5, 1)

diff = now - oneday

print(diff.days)
print(diff.total_seconds())

gap = datetime.timedelta(1)

tomorrow = now + gap
print(tomorrow)
