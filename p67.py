from datetime import datetime
startTime = datetime.now()

import pyperclip

pyr = pyperclip.paste()

#pyr = '''3
#7 4
#2 4 6
#8 5 9 3'''

pyr = pyr.split('\n')
pyr = [l.split() for l in pyr]
for k in range(len(pyr)):
    pyr[k] = [int(num) for num in pyr[k]]

def longest_slide_down(pyramid):
    for level in range(len(pyramid)-2, -1, -1):
        for k in range(len(pyramid[level])):
            pyramid[level][k] += max(pyramid[level+1][k], pyramid[level+1][k+1])
    return int(pyramid[0][0])

print(longest_slide_down(pyr))

print(datetime.now() - startTime)
