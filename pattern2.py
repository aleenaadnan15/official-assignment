#Question num 42:

''' The following pattern, using a nested for loop   '''

n = int(input("Enter no. of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

for i in reversed(range(1,n+1)):
    for j in range(1,i):
        print(j,end="")
    print("")
