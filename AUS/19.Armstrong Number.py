# Python program to check if a number is an Armstrong number

num = int(input("Enter the number you want to check: "))

num_digit = len(str(num))

sum_of_power = 0

temp = num

while temp > 0:
    digit = temp % 10
    sum_of_power = sum_of_power + digit ** num_digit
    temp = temp // 10

if sum_of_power == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")
    