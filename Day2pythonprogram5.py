n=int(input("Enter the size of pattern: "))
for i in range(n,0,-1):
    for j in range(0,i):
        if j==i-1:
            print(i)
        else:
            print(str(i)+"*",end="")
            
for i in range(1,n+1):
    for j in range(0,i):
        if j==i-1:
            print(i)
        else:
            print(str(i)+"*",end="")

