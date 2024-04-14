A = [[1, 2, 3, 4],

     [5, 6, 7, 8],

     [9, 10, 11, 12],

     [13, 14, 15, 16]]
transpose = []
for i in range(len(A)):
    transpose_col = []
    for j in range(len(A[i])):
        transpose_col.append(A[j][i])
    transpose.append(transpose_col)

print(transpose)

if A==transpose:
    print("Given matrix is Symmetry ")
else:
    print("Given matrix is not Symmetry")
