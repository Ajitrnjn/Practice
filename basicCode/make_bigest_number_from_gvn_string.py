
input_string='asfkjewnfekwlrj3435664'

temp_digit = ""
for i in input_string:
    value = ord(i)
    if 48 <= value <= 57:
        temp_digit = temp_digit + i

print(temp_digit)

print(sorted(temp_digit,reverse=True))

longest_digit= ""
for i in sorted(temp_digit,reverse=True):
    longest_digit = longest_digit+i

result_longest_number=int(longest_digit)
print(result_longest_number)

# x=5/4
# y=1/10
#
# print (int(x))
# print(int(y))

x = 541
reverse_num=0

while x != 0 :
    rem= x%10
    x = int(x/10)
    reverse_num = reverse_num*10 + rem

print(reverse_num)


# print(type(result_longest_number))
