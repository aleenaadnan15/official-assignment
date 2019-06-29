#Question num 28:

'''  Convert Octal number to Decimal number   '''

octal = input('enter octal num = ')
dec = 0
power = len(octal) - 1
for i in octal:
    dec += int(i) * 8 ** power 
    power = power - 1
print('decimal num:' ,dec)