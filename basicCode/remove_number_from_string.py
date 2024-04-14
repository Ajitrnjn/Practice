# Remove number from given input . Input = ' Ajit58912Raj ' , Output =  'AjitRaj'

str2 = 'Ajit58912Raj'
str3 = '934932Ajafdsfdklflkdslkf9989989'

def remove_number_from_string(input_string):
    temp_str = ""
    for i in input_string:
        if i.isdigit():

        #if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            continue
        else:
            temp_str = temp_str + i
    return temp_str

def remove_number_from_string_using_ascii(input_string):
    temp_str = ""
    for i in input_string:
        value = ord(i)
        if 48 <= value <= 57:

        #if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            continue
        else:
            temp_str = temp_str + i
    return temp_str

obtain_string = remove_number_from_string("gjghjghjg45645645646")
print(obtain_string)
print(remove_number_from_string_using_ascii("860958kjdkljglkdjfgjlkdf98098"))


#Remove Number From Array by using existing method



input_arr = ["Ajit58912Raj","gkjhkhk77897hjhkj","hghjgh45436gjhgjhg"]

res_array = []
for i in input_arr:
    res_array.append(remove_number_from_string(i))

print(res_array)

