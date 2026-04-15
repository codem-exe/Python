#Python Program to Merge Two Dictionaries

# Get input from user for two dictionaries
dict1 = eval(input("Enter first dictionary (e.g. {'a': 1, 'b': 2}): "))
dict2 = eval(input("Enter second dictionary (e.g. {'b': 3, 'c': 4}): "))

# Merging using the unpacking operator (Python 3.5+)
merged_dict = {**dict1, **dict2}

print("\nMerged Dictionary:", merged_dict)
