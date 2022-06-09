from datetime import datetime
startTime = datetime.now()

normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

counter = 0
day1st = 1       #the day of week of the first of the month, encoded mod 7
for year in range(1900, 2001):
    for month in range(0, 12):
        if day1st == 0 and year >= 1901:
            counter += 1
        if year % 4 != 0:
            day1st = (day1st + normal[month]) % 7
        if year % 4 == 0:
            day1st = (day1st + leap[month]) % 7
            
print(counter)

print(datetime.now() - startTime)
