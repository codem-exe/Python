# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end = " ")
#     print()

n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print("*",end= " ")
    print()

for i in range(n):
    for j in range(i,n):
        print("*",end= " ")
    print()