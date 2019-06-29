#Question num 24:

'''  sum of the first n positive integers   '''

n = int(input('enter positive integer = '))
sum = 1
for i in range (1, n+1):
    sum += i
print('sum' ,n, 'integer num' ,sum)