from datetime import datetime
startTime = datetime.now()

def sumOfDigs(num):
    s = 0
    for k in str(num):
        s += int(k)
    return s

print(sumOfDigs(2**1000))

print(datetime.now() - startTime)
