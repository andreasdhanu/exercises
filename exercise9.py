import datetime
sundays=0
start = datetime.date(1901, 1, 1)
while start <= datetime.date(2000, 12, 31):
    if start.weekday() is 6:
        sundays+=1
    start += datetime.timedelta(days=1)
print(datetime.date(2000, 12, 31).weekday())
print(sundays)

