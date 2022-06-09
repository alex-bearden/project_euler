def primeFactors(number):
    k=2
    primeFactors = [number]
    while k < primeFactors[-1]:
        if primeFactors[-1] % k == 0:
            primeFactors.insert(-1, k)
            primeFactors[-1] //= k
        else:
            k += 1
    return primeFactors
    

print(primeFactors(600851475143))
