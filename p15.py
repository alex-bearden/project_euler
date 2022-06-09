from datetime import datetime
startTime = datetime.now()

pat = []

for row in range(21):
    if row == 0:
        pat.append([1 for k in range(21)])
    else:
        newRow = [1]
        for k in range(1,21):
            newRow.append(newRow[k-1] + pat[row - 1][k])
        pat.append(newRow)

print(pat[20][20])


print(datetime.now() - startTime)
