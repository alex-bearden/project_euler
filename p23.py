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

abunNums = {n for n in range(1, 28124) if d(n) > n}

sumsOfAbuns = {i + j for i in abunNums for j in abunNums}
nsa = {n for n in range(1, 28124)} - sumsOfAbuns
print(sum(nsa))


print(datetime.now() - startTime)
