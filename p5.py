def primeFactors(number):
    primeFactors = [number]
    k=2
    while k < primeFactors[-1]:
        if primeFactors[-1] % k == 0:
            primeFactors.insert(-1, k)
            primeFactors[-1] //= k
        else:
            k += 1
    return primeFactors

def evenDiv(upper):
    currentFactors = []
    for k in range(2, upper + 1):
        for p in primeFactors(k):
            if currentFactors.count(p) < primeFactors(k).count(p):
                for n in range(1, primeFactors(k).count(p)-currentFactors.count(p)+1):
                    currentFactors.append(p)
    prod = 1
    for m in range(len(currentFactors)):
        prod *= currentFactors[m]
    return prod

print(evenDiv(20))
