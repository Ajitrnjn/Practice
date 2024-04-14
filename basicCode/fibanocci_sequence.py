
# Print first ten number fibanocci sequence

def Is_fibonacci_sequence(input_data):
    if input_data == 0:
        return 0

    if input_data == 1 or input_data == 2:
        return 1
    p = 0
    q = 1
    z = 0

    for i in range(2,input_data+1):
        z = p + q
        p = q
        q = z
    return z

input_data = int(input("Enter the number : "))
k=Is_fibonacci_sequence(input_data)

print("n'th Fibonacci sequence is : ",k)

