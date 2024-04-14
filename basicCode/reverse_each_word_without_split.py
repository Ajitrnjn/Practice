'ajit  raj'

from reverse_sentence import *

str1 = 'ajit raj jam'
length_str=len(str1)
print(length_str)
temp_str = ""
result_string =""
count = 0
for i in str1:
    # print(i)
    if i != ' ':
        temp_str = temp_str + i

    count +=1

    # print(temp_str)

    if i == ' ' or count == length_str:
        # print("inside string")
        revers_str = reverse_string(temp_str)
        temp_str = ""
        result_string = result_string + revers_str +" "

    # count +=1

print(result_string)
