from datetime import datetime
startTime = datetime.now()

def d(number):
    divisors = {1}
    for k in range(2,number):
        if k in divisors:
            continue
        elif number % k == 0:
            divisors.add(k)
            divisors.add(number // k)
    return sum(divisors)

s = 0
for a in range(1,10000):
    if d(d(a)) == a and a != d(a):
        s += a

print(s)

print(datetime.now() - startTime)
