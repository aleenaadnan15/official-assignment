#Question num 19:

''' convert the distance (in feet) to inches, yards, and miles   '''

feet = int(input('enter distance in feet = '))
inches = feet * 12
yards = feet / 3
miles = feet / 5280
print('distance in inches:' ,inches)
print('distance in yards:' ,yards)
print('distance in miles:' ,miles)