def total(k):
    total = 0
    for l in range(1,k+1):
        total += l
    return total

def sumSquare(k):
    total = 0
    for l in range(1,k+1):
        total += l**2
    return total

print(total(100)**2 - sumSquare(100))
