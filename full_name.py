#Question  num 33:
 
'''  First and last name in  reverse order with a space between them  '''

f_name = input('enter first name = ')
l_name = input('enter last name = ')

for f in reversed(f_name):
    print(f,end="")
print(end=" ")
for l in reversed(l_name):
    print(l,end="") 