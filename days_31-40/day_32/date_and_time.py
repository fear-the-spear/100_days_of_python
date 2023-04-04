import datetime as dt

# Get current date and time
now = dt.datetime.now()  # 2023-03-30 20:44:52.928185
# get year
year = now.year  # 2023
# get month
month = now.month  # 3 <- March
# get weekday
day_of_week = now.weekday()  # 3 <- Thursday

date_of_birth = dt.datetime(year=1991, month=10, day=16, hour=16, minute=34)
print(date_of_birth)
