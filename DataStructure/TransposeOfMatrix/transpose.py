A = [[1, 2, 3, 4],

     [5, 6, 7, 8],

     [9, 10, 11, 12],

     [13, 14, 15, 16]]

tr = []
for i in range(len(A)):
    tr_col = []
    for j in range(len(A[i])):
        tr_col.append(A[j][i])
    tr.append(tr_col)

print(tr)
