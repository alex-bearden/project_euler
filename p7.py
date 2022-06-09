from datetime import datetime
startTime = datetime.now()

def isPrime(number):
    k=2
    while k <= number**(.5):
        if number % k == 0:
            return False
            break
        else:
            k += 1
    return True

def nthPrime(n):
    if n == 1:
        return 2
    else:
        prime = 3
        cand = 3
        for k in range(2,n+1):
            while isPrime(cand) == False:
                cand = cand + 2
            prime = cand
            cand = cand + 2
        return prime

print(nthPrime(10001))
            
print(datetime.now() - startTime)
