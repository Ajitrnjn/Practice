# Reverse each word of sentence. Input : I am boy. output : I ma yob

# take the character from the user
# char_input = input(" Hey Ajit enter the character : ")
# print(char_input)
#
# split_char_input = char_input.split( " ")
# print(split_char_input)

from reverse_sentence import *


def reverse_each_of_sentence(input_str):
    str_arr = input_str.split(" ")              # split around space
    result_str = ""
    for st in str_arr:
        reversed_str = reverse_string(st)              # call the user define function
        result_str = result_str + reversed_str + " "

    return result_str


input_string = input("Enter the sentence : ")
res = reverse_each_of_sentence(input_string)

print(res)

