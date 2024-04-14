A = [[1, 2, 3, 4],

     [5, 6, 7, 8],

     [9, 10, 11, 12],

     [13, 14, 15, 16]]

# print(A[0][2])
# print(A[1][2])
# print(A[2][2])
# print(A[3][2])

#print the middle column element

column_length = len(A[0])

for i in range(len(A)):
    print(A[i][int(column_length/2)])



for i in A:
    for j in i:
        print(j, end=" ")
    print()

print("index based printing ")

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=" ")
    print()

print("Print Left diagonal element : ")

for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            print(A[i][j], end=" ")

    print()


print("Print Right diagonal element : ")

col_length = len(A[0])
for i in range(len(A)):
    # for j in range(len(A)):
        print(A[i][col_length-1-i], end=" ")

    # print()

print("Rotate the matrix 90-degree AntiClockwise")

for i in range(len(A[0])-1,-1,-1):
    for j in range(len(A)):
        print(A[j][i], end= " ")
    print()

print("Rotate the matrix 90 - degree Clockwise")

# for i in range(len(A)-1,-1,-1):
#     for j in range (len(A[0])):
#         print(A[j][i], " ")
#     print()


print( A[int(len(A)/2)])


#Rotate matrix 90degree clock-wise and anti-clockwise .
#Transpose of matrix
#Print middle row of matrix and middle column of matrix
#Mirroe Image of matrix
#Check the symmetry of matrix