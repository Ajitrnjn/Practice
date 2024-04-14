# factorial calculation
def find_factorial(n):
    k = 1
    for i in range(1, n + 1):
        k = i * k

    return k

n = int(input("Enter the number : "))
result = find_factorial(n)
print("factorial of given number is  : ", result)


