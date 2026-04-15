# Python Program to Transpose a Matrix

# Taking input for matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input the matrix
print("\nEnter elements of the matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix.append(row)

# Transposing the matrix
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

# Displaying the transpose
print("\nTransposed Matrix:")
for row in transpose:
    print(row)


