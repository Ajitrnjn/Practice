print("Try programiz.pro")

n = int(input("enter the number of rows : "))

for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i + 1):
        print(j+1, end=" ")

    print()