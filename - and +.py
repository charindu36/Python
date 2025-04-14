# left side

n=5
for i in range(n):
    for j in range(i,n):
        print("- ",end=" ")
    for k in range(i+1):
        print(" +",end=" ")    
    print()

#right side

n=5
for x in range(n):
    for i in range(x+1):
        print("+ ",end=" ")
    for j in range(x,n):
        print(" -",end=" ")    
    print()     