Employee = {"Name": "John", "Age": 29, "salary": 25000, "Company": "WIPRO"}
for x in Employee:
    print(Employee[x])

import time;

# returns a time tuple

print(time.localtime(time.time()))

import time

# returns the formatted time

print(time.asctime(time.localtime(time.time())))

import calendar

#printing the calendar of the year 2019
s = calendar.prcal(2024)
