# first method

n=5
for x in range(n):
    for i in range(n-x):
        print("*",end=" ")
    print()

#second method

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()     
