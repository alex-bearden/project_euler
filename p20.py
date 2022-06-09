from datetime import datetime
startTime = datetime.now()

import math

num = math.factorial(100)

s = 0

for n in str(num):
    s += int(n)

print(s)

print(datetime.now() - startTime)
