# Python Program to Find Armstrong Number in an Interval

start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

print(f"Armstrong Numbers between {start} and {end}")

for num in range(start, end + 1):
    num_digit = len(str(num))
    sum_of_power = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_power += digit ** num_digit
        temp = temp // 10

    if sum_of_power == num:
        print(num)