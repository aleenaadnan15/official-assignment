#Question num 16:

'''   Compute the distace b/w two point   '''

import math

x1 = int(input('enter value x1='))
y1 = int(input('enter value y1='))
x2 = int(input('enter value x2='))
y2 = int(input('enter value y2='))

distance = round(math.sqrt( math.pow( (x2-x1) ,2) + math.pow( (y2-y1) ,2)) ,2)
print('distance b/w two point is:' , distance)