#Question num 15:

'''  compute the future value of a specified principal amount, rate of interest, and a number of years   '''

p = int(input('enter principal amount'))
r = float(input('enter rate of interest'))
t = int(input('enter num of years'))

A = p *(1+(r*t))

print('future value =' ,A)
