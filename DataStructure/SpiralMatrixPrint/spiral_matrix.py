# A = [[1, 2, 3, 4],
#
#      [5, 6, 7, 8],
#
#      [9, 10, 11, 12],
#
#      [13, 14, 15, 16]]


def print_spiral_matrix(matrix):
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    row_start, row_end = 0, rows - 1
    col_start, col_end = 0, cols - 1

    while row_start <= row_end and col_start <= col_end:
        # Print top row
        for j in range(col_start, col_end + 1):
            print(matrix[row_start][j], end=" ")
        row_start += 1

        # Print right column
        for i in range(row_start, row_end + 1):
            print(matrix[i][col_end], end=" ")
        col_end -= 1

        # Print bottom row (if not already printed)
        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                print(matrix[row_end][j], end=" ")
            row_end -= 1

        # Print left column (if not already printed)
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                print(matrix[i][col_start], end=" ")
            col_start += 1


# Example matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nMatrix printed in spiral form:")
print_spiral_matrix(matrix)
