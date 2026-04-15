# Python Program to Find the Sum of Natural Numbers

num = int(input("Enter a number: "))

sum_natural_num = 0

if num < 0:
    print("Please enter a positive number")
else:
    for i in range(1, num+1):
        sum_natural_num+=i

    print("Sum of natural numbers is",sum_natural_num)