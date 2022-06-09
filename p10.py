from datetime import datetime
startTime = datetime.now()

def isPrime(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    elif number % 3 == 0:
        return False
    else:
        k=5
        while k <= number**(.5):
            if number % k == 0 or number % (k+2) == 0:
                return False
                break
            else:
                k += 6
        return True

rsum = 0
for k in range(1,2000000):
    if isPrime(k) == True:
        rsum += k

print(rsum)
print(datetime.now() - startTime)
