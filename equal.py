#Question num 13:
'''    True if the two given integer values are equal or their sum or difference is 5   ''' 

num1 = int(input('enter first num:'))
num2 = int(input('enter second num:'))

if num1 == num2:
    print('two nums are equal' + ' true')
elif num1 + num2 == 5:
    print('sum of two nums is: 5' + ' true')
elif num1 - num2 == 5:
    print('difference of two nums is: 5' + ' true')
else:
    print('false')