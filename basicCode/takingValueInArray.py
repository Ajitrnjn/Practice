#code snippet for taking array element in specific length by user

from array import *

arr = array("i",[])

n = int(input("Enter the length of the array : "))

for i in range(n):
    x=int(input("Enter the next value "))
    arr.append(x)

print(arr)

#write a code for finding the index of array in given array

val=int(input("enter the value for which you want the index :"))
k=0
for z in arr:
    if z==val:
        print("index of the search value is :",k)
        break
    k+=1