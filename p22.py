from datetime import datetime
startTime = datetime.now()

import pyperclip

nameList = sorted(pyperclip.paste().split(','))
nameList = [n.strip('\"') for n in nameList]

s = 0
for ind, name in enumerate(nameList):
    s += (ind + 1) * sum([ord(l) - 64 for l in name])

print(s)

print(datetime.now() - startTime)
