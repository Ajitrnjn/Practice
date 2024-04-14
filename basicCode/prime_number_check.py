# write the code for given number is prime or not .

# x=12
# count = 0
# for i in range(2,int(x/2)+1,1):
#     if x % i == 0:
#         count += 1
#         if count == 3:
#             break
#
# if count == 3:
#     print("number is not prime")
# else:
#     print("number is prime")


n = int(input("Enter the value : "))
isPrime = True

def Is_number_prime(n):
    if n == 2 or n == 1:
        return isPrime
    for i in range(2, int(n / 2), 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime


is_prime = Is_number_prime(n)

print("Given number is  prime : ", is_prime)

