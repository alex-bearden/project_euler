from datetime import datetime
startTime = datetime.now()

def primeFactors(number):
    k=2
    primeFactors = [number]
    while k <= primeFactors[-1]**0.5:
        if primeFactors[-1] % k == 0:
            primeFactors.insert(-1, k)
            primeFactors[-1] //= k
        else:
            k += 1
    return primeFactors

def uniquePrimeFactors(number):
    unPrF = []
    for k in primeFactors(number):
        if k in unPrF:
            continue
        else:
            unPrF.append(k)
    return unPrF

def numOfDivisors(number):
    numsOfPrimes = [] # a list of the number of each distinct prime factor
    for k in uniquePrimeFactors(number):
        numsOfPrimes.append(primeFactors(number).count(k))
    numOfDiv = 1
    for n in numsOfPrimes:
        numOfDiv *= n + 1
    return numOfDiv


n=1
while True:
    if numOfDivisors(int(n*(n+1)/2)) <= 500:
        n += 1
    else:
        print(int(n*(n+1)/2))
        break

print(datetime.now() - startTime)
