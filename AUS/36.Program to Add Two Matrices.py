# Python Program to Add Two Matrices

# Define the size of the matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input for first matrix
print("\nEnter elements for the first matrix:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix1.append(row)

# Input for second matrix
print("\nEnter elements for the second matrix:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i}][{j}]: ")))
    matrix2.append(row)

# Adding the matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Displaying the result
print("\nResultant Matrix after Addition:")
for row in result:
    print(row)
