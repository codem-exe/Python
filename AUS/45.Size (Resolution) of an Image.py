# 45. Python Program to Find the Size (Resolution) of an Image

from PIL import Image

# Ask user to enter image file path
file_path = input("Enter the path to the image file: ")

try:
    with Image.open(file_path) as img:
        width, height = img.size
        print(f"\nImage Resolution: {width} x {height} pixels")
except FileNotFoundError:
    print("File not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")
