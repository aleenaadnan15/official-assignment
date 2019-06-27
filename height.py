#Question num 17:

'''  Convert height (in feet and inches) to centimetres  '''

height_feet = int(input('enter height in feet='))
height_inches = int(input('enter height in inches='))

height_centi1 = height_feet * 30.48
height_centi2 = height_inches * 2.54

print('total height in cm:' , height_centi1 + height_centi2)
