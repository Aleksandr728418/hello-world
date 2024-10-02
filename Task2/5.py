import datetime

hour = int(input("What hour (24hr) were you born?\n"))
day = int(input("What day (number) of the month were you born?\n"))
month = int(input("What number month were you born?\n"))
year = int(input("What year were you born?\n"))

# create a new datetime object with user input
birth_datetime = datetime.datetime(year, month, day, hour)
# get current datetime
current_datetime = datetime.datetime.now()
# compute the difference
diff = current_datetime - birth_datetime

# convert days (*24) and seconds (/3600) to hours and sum 
hours = diff.days*24 + diff.seconds/3600

print(f"Your age in hours is {round(hours)}.")
