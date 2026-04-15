#  Python Program to Multiply Two Matrices

# Input number of rows and columns for first matrix
rows1 = int(input("Enter rows for Matrix A: "))
cols1 = int(input("Enter columns for Matrix A: "))

# Input number of rows and columns for second matrix
rows2 = int(input("Enter rows for Matrix B: "))
cols2 = int(input("Enter columns for Matrix B: "))

# Check if multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication not possible! ❌ Columns of A must equal rows of B.")
else:
    # Input Matrix A
    print("\nEnter elements for Matrix A:")
    A = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)

    # Input Matrix B
    print("\nEnter elements for Matrix B:")
    B = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)

    # Initialize result matrix with 0s
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Matrix Multiplication Logic
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):  # or rows2 (same value)
                result[i][j] += A[i][k] * B[k][j]

    # Display the result
    print("\nResultant Matrix after Multiplication:")
    for row in result:
        print(row)
