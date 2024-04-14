# find the middle string of given character

# take the character from the user

char_input = input(" Hey Ajit enter the character : ")
print(char_input)

count = 0

for k in char_input:
    print(k)
    count += 1
print(count)

mid_index = int(count / 2)

print("middle element:", char_input[mid_index])

print()


# With the help of function help:
def middle_elment(char_input):
    count = 0
    for k in char_input:
        print(k)
        count += 1
    print(count)

    mid_index = int(count / 2)

    print("middle element:", char_input[mid_index])
middle_elment(char_input)
