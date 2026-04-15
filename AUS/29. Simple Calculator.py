# Python Program to Make a Simple Calculator

print("--------------CALCULATOR----------------")
print()
print("Which operation do you want to perform: ")
print("Addition ----------------------------- +")
print("Subtraction -------------------------- -")
print("Multiplication------------------------ *")
print("Division------------------------------ /")
print()
choice = input("Enter your choice (+,-,*,/): ")

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Cannot Divide by Zero"
    else:
        return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "+":
    print(f"The sum of {num1} + {num2} = ",add(num1,num2))
if choice == "-":
    print(f"The subtraction of {num1} - {num2} = ",subtract(num1,num2))
if choice == "*":
    print(f"The multiplication of {num1} * {num2} = ",multiply(num1,num2))
if choice == "/":
    print(f"The division of {num1} / {num2} = ",divide(num1,num2))
