n= int(input("Enter the size of the pattern: "))

for i in range(n):
    for j in range(n):
        if (i == j) or ((n-1-j) == i):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print("")

