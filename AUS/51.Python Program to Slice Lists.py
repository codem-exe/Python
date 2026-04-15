# Python Program to Slice Lists

# Taking input from the user
user_input = input("Enter elements separated by commas: ").split(',')

# Clean up whitespace
my_list = [item.strip() for item in user_input]

print("\nOriginal List:", my_list)

# Start, stop, step input
start = int(input("Enter start index: "))
stop = int(input("Enter stop index: "))
step = int(input("Enter step (use 1 if unsure): "))

# Slicing the list
sliced = my_list[start:stop:step]

print("\nSliced List:", sliced)
