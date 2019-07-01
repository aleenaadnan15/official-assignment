#Question num 43:

''' The following pattern, using a nested for loop   '''

n = int(input('enter num = '))

for i in range(n):
    for j in range(1, i + 1):
        print(i, end = "")
    print("")