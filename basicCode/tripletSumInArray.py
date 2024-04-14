# Given an array and number , find two number array such sum two number is equal to given number

# [3,4,5 7]

from array import *

gvn_array = [12, 3, 4, 1, 6, 9]
gvn_number = int(input("enter the number : "))

z = len(gvn_array)
print("length of array :" , z)

is_Somethere = 0

for i in range(len(gvn_array)-2):
    for j in range(i+1 , z):
        for k in range(j+1 , z):
        # if i < z:
            if gvn_number == gvn_array[i] + gvn_array[j] + gvn_array[k]:
                print(gvn_array[i],gvn_array[j],gvn_array[k])
                is_Somethere = 1

if is_Somethere == 0:
    print("not found")
else:
    print("found")


# write the code for , Print the two number combination from given array which is equal to target number

nums = [2, 7, 11, 15]
k = len(nums)
target = 9
Is_somethere = 0
for i in range(0, k):
    # if i < k:
    for j in range(i + 1, k):
        if target == nums[i] + nums[j]:
            print(nums[i], nums[j])
            Is_somethere = 1

if Is_somethere != 0:
    print("found")
else:
    print("not found")