#Question num 26:

'''  convert an integer to Binary, Octal and Hexadecimal numbers   '''

decimal = int(input('enter decimal num = '))

#Binary: 
binary = ""
while decimal > 0:
        rem = decimal % 2
        decimal = decimal // 2
        binary = str(rem) + binary
print("binary num =",binary)

#Octal:
decimal = int(input('enter decimal num = '))
octal = ""
while decimal > 0:
        rem = decimal % 4
        decimal = decimal // 4
        octal = str(rem) + octal
print("octal num =",octal)

#Hexadecimal:
decimal = int(input("enter decimal num =  "))
hexadecimal = ""
while decimal > 0:
        rem = decimal % 8
        decimal = decimal // 8
        hexadecimal = str(rem) + hexadecimal
print("hexadecimal num =",hexadecimal) 