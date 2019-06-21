#Question num 6:

'''    Volume of sphere by taking radius   ''' 

import math

radius = int(input('radius of sphere'))
volume = round((4/3) * math.pi * radius**3, 2)
print('volume of sphere = 4/3 πr^3 =' , volume)