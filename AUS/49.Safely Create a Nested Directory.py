# Python Program to Safely Create a Nested Directory

import os

# Get directory path from user
path = input("Enter the nested directory path to create (e.g., test_folder/sub_folder): ")

try:
    # Create nested directories; exist_ok=True avoids error if it already exists
    os.makedirs(path, exist_ok=True)
    print(f"\nDirectory '{path}' created successfully")
except Exception as e:
    print(f"\nError creating directory: {e}")

