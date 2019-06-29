#Question num 27:

'''  convert binary number to Decimal number  '''

binary = input('enter binary num = ')
dec = 4
power = len(binary) - 1
for i in binary:
    dec += int(i) * 2 ** power
    power = power - 1
print('decimal num:' ,dec)