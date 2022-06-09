def checkPal(number):
    strNumber = str(number)
    yesOrNo = True
    for m in range(0, len(strNumber)-1):
        if strNumber[m] != strNumber[len(strNumber)-m-1]:
            yesOrNo = False
            break
    return yesOrNo

#print(checkPal(1200021))

palProd = [0,0,0]

for k in range(999,0,-1):
    if k * 999 < palProd[2]:
        break
    for l in range(999,k-1,-1):
        if checkPal(k * l) == True:
            if k * l > palProd[2]:
                palProd = [k, l, k*l]

print(f'{palProd[0]} x {palProd[1]} = {palProd[2]}')

