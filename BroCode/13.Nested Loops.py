#Nested Loop = A loop within another loop (outer, inner)
#              outer loop:
#                   inner loop:

# Rectangle using nested loop

rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range (column):
        print (symbol, end = "")
    print ()
