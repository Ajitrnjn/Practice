A = [[1, 2, 3, 4],

     [5, 6, 7, 8],

     [9, 10, 11, 12],

     [13, 14, 15, 16]]
# print(A[0])
# mirror_image = []
#
#
# def rev_row(i):
#     for k in range(len(i)):
#         # i[0],i[len-1] = i[len-1],i[0]
#         if k < len(i) / 2:
#             i[k], i[len(i) - k - 1] = i[len(i) - k - 1], i[k]
#         else:
#             break
#     return i
#
#
# for i in A:
#     reversed_row = rev_row(i)
#     mirror_image.append(reversed_row)
#
# print(mirror_image)

print("Horizontally mirror image ")

column_length = len(A[0])
row_length = len(A)
for k in range(column_length):
    for i in range(int(len(A)/2)):
        print(A[i][k], A[row_length - 1 - i][k])
        print(
            '-----------------------------------'
        )
        A[i][k], A[row_length-1-i][k] = A[row_length-1-i][k],A[i][k]


print(A)