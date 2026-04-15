# Python Program to Check Whether a String is Palindrome or Not

def is_palindrome(string):
    # Remove spaces and convert to lowercase for fair comparison
    string = string.replace(" ", "").lower()
    return string == string[::-1]

# Input from user
text = input("Enter a string: ")

# Check and print result
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
