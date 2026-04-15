# Python Program to Find Sum of Natural Numbers Using Recursion
def sum_natural(n):
    if n <= 1:
        return n
    return n + sum_natural(n - 1)

# Input from user
num = int(input("Enter a positive integer: "))

if num < 0:
    print("Oops! Please enter a positive number")
else:
    total = sum_natural(num)
    print(f"The sum of natural numbers up to {num} is: {total}")
