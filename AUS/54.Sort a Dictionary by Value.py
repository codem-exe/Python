# Step 1: Take user input for dictionary
user_dict = {}
n = int(input("How many key-value pairs do you want to enter? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for '{key}': "))  # assuming numerical values for sorting
    user_dict[key] = value

print("\nOriginal Dictionary:")
print(user_dict)

# Step 2: Sort by values (ascending)
sorted_dict_asc = dict(sorted(user_dict.items(), key=lambda item: item[1]))
print("\nSorted by Value (Ascending):")
print(sorted_dict_asc)

# Step 3: Sort by values (descending)
sorted_dict_desc = dict(sorted(user_dict.items(), key=lambda item: item[1], reverse=True))
print("\nSorted by Value (Descending):")
print(sorted_dict_desc)
