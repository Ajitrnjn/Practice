# Finding the factorial of given number using the recursion

def fact_using_recursion( n ):
    if (n == 0):
        return 1
    return n * fact_using_recursion(n - 1)
    # k= n * fact_using_recursion(n - 1)
    # return k


n = int(input("Enter the number : "))
result = fact_using_recursion(n)

print("factorial of given number is  : ", result)
print("factorial of given number upto only 4 digit is  : ", str(result)[:4])

