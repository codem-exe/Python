# Python Program to Find Hash of File

import hashlib

def hash_file(filename):
    """Return the SHA256 hash of the file"""
    h = hashlib.sha256()

    try:
        with open(filename, 'rb') as file:
            chunk = file.read(4096)
            while chunk:
                h.update(chunk)
                chunk = file.read(4096)
        return h.hexdigest()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Input from user
file_path = input("Enter the path to the file: ")
file_hash = hash_file(file_path)

print(f"\nSHA256 Hash: {file_hash}")
