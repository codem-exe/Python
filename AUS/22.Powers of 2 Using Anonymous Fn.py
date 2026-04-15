# Python Program to Display Powers of 2 Using Anonymous Function

num = int(input("Enter a number: "))

power = lambda x: x**2

for i in range(1, num+1):
    print(f"Power of {i} is {power(i)}")