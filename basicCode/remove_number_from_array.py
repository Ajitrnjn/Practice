

def remove_number_from_array(input_array):
    result_array = []
    temp_str = ""
    for i in input_array:
        for j in i:
            if j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9':
                continue
            else:
                temp_str = temp_str + j
        result_array.append(temp_str)
        temp_str=" "



    return result_array
obtain_array=remove_number_from_array(input_array=['asfghj876654','aghjkhyui34567', 'fghjkju4567'])
print(obtain_array)