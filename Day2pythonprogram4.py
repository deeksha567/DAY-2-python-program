n = int(input("Enter the size of patter: "))
for i in range(0, n):
    print("*" * (n - i) + "  " * i + "*" * (n - i))
for j in range(2, n+1):
    print("*" * j + "  " * (n - j) + "*" * j)
