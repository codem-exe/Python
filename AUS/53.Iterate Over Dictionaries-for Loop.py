# Create an empty dictionary
user_dict = {}

# Ask user how many items they want to enter
n = int(input("How many key-value pairs do you want to enter? "))

# Loop to take user input
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    user_dict[key] = value

print("\nYour Dictionary:")
print(user_dict)

print("\n🔹 Iterating over keys:")
for key in user_dict:
    print(key)

print("\n🔹 Iterating over values:")
for value in user_dict.values():
    print(value)

print("\n🔹 Iterating over key-value pairs:")
for key, value in user_dict.items():
    print(f"{key} ➝ {value}")
