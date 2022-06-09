from datetime import datetime
startTime = datetime.now()

import pyperclip

nums = pyperclip.paste()
nums = nums.split()
nums = [int(n) for n in nums]
sumOfNums = sum(nums)

firstTen = ''
for k in range(0,10):
    firstTen += str(sumOfNums)[k]

print(firstTen)

print(datetime.now() - startTime)
