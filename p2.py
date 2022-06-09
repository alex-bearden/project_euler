fib = [1,2]
count = 0

while True:
    if fib[0]%2 == 0:
        count += fib[0]
    fib = [fib[1], fib[0]+fib[1]]
    if fib[0] > 4000000:
        break

print(count)
