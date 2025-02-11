import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
print(f"Today: {today.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
