#Question num 31:

'''  Compute the GCD of two positive integer  '''
 
num1 = int(input('enter any integer num = '))
num2 = int(input('enter any integer num = '))

i = 1
while (i <= num1 and i <= num2):
    if ((num1 % i) == 0 and (num2 % i) == 0) :
        gcd = i
    i = i + 1
print("The GCD of {0} & {1} = {2}".format(num1,num2,gcd))
