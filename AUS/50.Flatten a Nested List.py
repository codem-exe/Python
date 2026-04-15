# Python Program to Flatten a Nested List

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # recursive call
        else:
            flat_list.append(item)
    return flat_list

import ast
user_input = input("Enter a nested list (e.g., [1, [2, [3, 4], 5], 6]): ")
nested_list = ast.literal_eval(user_input)  # safely convert string to list

flat = flatten_list(nested_list)
print("\nFlattened List:", flat)
