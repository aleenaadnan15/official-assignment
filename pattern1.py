#Question num 41:

'''  The following pattern, using a nested for loop   '''

n = int(input("Enter no. of rows: "))
for i in range (0,n):
    for j in range (0,i):
        print("*",end="")
    print("")

for i in reversed(range(0,n+1)):
    for j in range(0,i):
        print("*",end="")
    print("")
