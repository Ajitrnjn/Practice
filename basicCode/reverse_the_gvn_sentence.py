# Hey Ajit , reverse this sentence . output: Ajit Hey, take input from user

#Block1: Taken sentence from user

usr_input = input("Hey Ajit Enter the sentence:")
print(usr_input)
print(type(usr_input))

#Block2 :
# for sentence in splitted_input:

splitted_input = usr_input.split(" ")
print(splitted_input)
print(type(splitted_input))

k = len(splitted_input)
print("length of the string : ",k)

reverse_sentence = " "

for i in range(k-1,-1,-1):
    print((i))

    if i <= k:
        reverse_sentence = reverse_sentence + (splitted_input[i]) + " "
        # print(reverse_sentence)
print("The Reverse Sentence is : ", reverse_sentence)
        # break










