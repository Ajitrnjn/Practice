matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

row_length = len(matrix)
col_length = len(matrix[0])
row_start, row_end = 0, row_length - 1
col_start, col_end = 0, col_length - 1

while row_end >= row_start and col_length:
