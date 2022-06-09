from datetime import datetime
startTime = datetime.now()

#NOT USED:
def chainLength(num):
    l = 1
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = 3 * num + 1
        l += 1
    return l

#print(chainLength(1000000))

#KEEPS TRACK OF ANY NUMBERS THAT HAVE ALREADY BEEN HIT:
setToSkip = {0}

winner = 0
maxLength = 0
for k in range(1,1000001):
    if k in setToSkip:
        continue
    else:
        num = k
        l = 1
        while num != 1:
            if num % 2 == 0:
                num = num//2
                setToSkip.add(num)
            else:
                num = 3 * num + 1
                setToSkip.add(num)
            l += 1
        if l > maxLength:
            maxLength = l
            winner = k

print(winner)
print(maxLength)

print(datetime.now() - startTime)
