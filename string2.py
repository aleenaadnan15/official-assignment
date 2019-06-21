#Question num 9:

'''   copies of a given string   '''

string = input('enter any string')
n = int(input('enter a non-neg integer'))
copies = (string + '\n') * n

print(copies)