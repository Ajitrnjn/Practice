#find the duplicate number in given array by loop method


from array import *

gvn_array = [3,5,4,3,6,4,8,5,6]

len_array=len(gvn_array)

for i in range(len_array):
    for j in range(i+1,len_array):
        if gvn_array[i]==gvn_array[j]:
            print("duplicate element : ", gvn_array[i])

