#Question num 32:

'''  Get the LCM of two positive integer  '''

num1 = int(input('enter integer num = '))
num2 = int(input('enter integer num = '))

i = 1
while (i <= num1 and i <= num2):
    if (num1 % i) == 0 and (num2 % i) == 0:
        lcm = i
    i = i + 1
print("The LCM of {0} and {1} = {2}" .format(num1,num2,lcm))
