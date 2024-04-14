# Given an array and number , find two number array such sum two number is equal to given number

# [3,4,5 7]

from array import *

gvn_array= [12, 3, 4, 1, 6, 9]
gvn_number=int(input("enter the number : "))

z=len(gvn_array)
print("length of array :",z)

isomethere = 0

for i in range(len(gvn_array)):
    for j in range(i+1,z):
        if i < z:
            if gvn_number == gvn_array[i] + gvn_array[j]:
                print(gvn_array[i],gvn_array[j])
                isomethere = 1

if isomethere == 0:
    print("not found")
else:
    print("found")
