#Question num 29:

'''   Convert Hexadecimal number to Decimal number   '''

hexadecimal = input('enter hexa num = ')

dec = 0
power = len(hexadecimal) - 1
for i in hexadecimal:
    dec += int(i) * 10 ** power 
    power = power - 1
print('decimal num:' ,dec)