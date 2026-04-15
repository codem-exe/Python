# Python Program to Display the Multiplication Table

num = int(input("Enter a Number: "))

for i in range (1,11):
    ans = num * i
    print(f"{num} x {i} = {ans}")