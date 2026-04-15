# Python Program to Find Numbers Divisible by Another Number

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
divisor = int(input("Enter the divisor: "))

print(f"Numbers divisible by {divisor} between {lower} and {upper} are:")

for num in range (lower, upper+1):
    if num % divisor == 0:
        print(num)