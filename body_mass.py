#Question num 22:

''' calculate body mass index  '''

weight = int(input('enter your body weight in kg = '))
height = int(input('enter your height in feet = '))

height = height/100

body_mass = (weight/height**2)
print('your body_mass result:' ,body_mass)

if body_mass < 20:
    print("You are Underwight")
elif body_mass >= 20 and body_mass < 24.9:
    print("You are Normal Weight")
elif body_mass >= 25 and body_mass < 29.9:
    print("You are Overweight")
elif body_mass >= 30 and body_mass < 34.9:
    print("You are Class I")
elif body_mass >= 35 and body_mass < 49.9:
    print("You are Class II")
elif body_mass >= 50:
    print("You are Class III") 