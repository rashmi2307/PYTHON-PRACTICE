n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    
    # print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # print stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()


