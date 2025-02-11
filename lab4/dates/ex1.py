import datetime

x = datetime.datetime.now()
print(f"The current date: {x.strftime('%x')}")

x = x-datetime.timedelta(days = 5)
print(f"The date 5 days ago: {x.strftime('%x')}")