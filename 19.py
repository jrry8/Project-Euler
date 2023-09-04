# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

# 1 Jan 1901 = Tuesday
# 6 Jan 1901 = Sunday

numDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysToSunday = 5
res = 0

for year in range(1901, 2001):
    for month in range(12):
        if (daysToSunday == 0):
            res += 1
        inc = numDays[month]
        if (month == 1):
            if (year % 4 == 0):
                if (year % 100 == 0):
                    if (year % 400 == 0):
                        inc += 1
                else:
                    inc += 1
        inc = inc % 7
        daysToSunday -= inc
        if (daysToSunday < 0):
            daysToSunday += 7

print(res)
