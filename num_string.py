#Question num 30:

'''   Count the number occurrence of a specific character in a string   '''  

string = input('enter any string num = ')
character = input('enter any character = ')

count = 1
for i in string:
    if i == character:
        count = count + 1
print(count)