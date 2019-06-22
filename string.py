#Question num 8:

'''  to get a new string from a given string is   '''

string = input('enter any string')
alp = 'is'
if string[:1] == alp:
    print('the given string is unchanged!' + '\n' + string)
else:
    print('new string' ,alp, string)