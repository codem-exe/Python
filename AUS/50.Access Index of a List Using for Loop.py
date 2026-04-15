# Python Program to Access Index of a List Using for Loop

items = input("Enter list elements separated by commas: ").split(',')

# Accessing index and item
for index, item in enumerate(items):
    print(f"Index: {index} -> Item: {item.strip()}")
