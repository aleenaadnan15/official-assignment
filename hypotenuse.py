#Question num 18:

''' calculate the hypotenuse of a right angled triangle  '''

import math

a = int(input('enter base of right angle triangle ='))
b = int(input('enter height of right angle triangle ='))

hypotenuse = round(math.sqrt(a**2 + b**2) ,2)
print('hypotenuse of right angle triangle:' ,hypotenuse)