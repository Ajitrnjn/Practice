# Reverse the given word . Input : Ajit , Output : tijA

# take the character from the user
# char_input = input(" Hey Ajit enter the character : ")
# print(char_input)


# Got the character .Now print each letter

# for i in range(len(char_input)):
#     # print(i) , #shows that at each value of i what character print
#     print(char_input[i])
#
# print()


#
# for i in char_input:
#     print(i)

# print(reverse_char)


def reverse_string(input_str):
    reverse_char = ""
    for k in range(len(input_str) - 1, -1, -1):
        reverse_char = reverse_char + input_str[k]
    return reverse_char

# print(reverse_string("shekhar"))
