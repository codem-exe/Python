# Python Program to Swap Two Variables

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the seocnd number: "))

temp = num1
num1 = num2
num2 = temp

print(f"Now the first number is: {num1}")
print(f"And the second number is: {num2}")