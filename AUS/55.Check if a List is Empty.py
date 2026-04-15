# Ask the user how many elements they want to enter
n = int(input("How many elements do you want to add to the list? "))

# Create the list based on input
user_list = []

if n == 0:
    print("The list is empty.")
else:
    for i in range(n):
        item = input(f"Enter item {i+1}: ")
        user_list.append(item)

    # Final check
    if not user_list:
        print("The list is empty.")
    else:
        print("The list is NOT empty.")
        print("List contents:", user_list)
