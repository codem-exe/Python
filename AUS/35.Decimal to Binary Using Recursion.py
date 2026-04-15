# Python Program to Convert Decimal to Binary Using Recursion

def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary: 0")
elif num < 0:
    print("Please enter a non-negative number!")
else:
    binary = decimal_to_binary(num)
    print(f"Binary of {num} is: {binary}")
