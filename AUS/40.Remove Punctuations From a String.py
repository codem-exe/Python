# Python Program to Remove Punctuations From a String

import string

# Define punctuation characters
punctuations = string.punctuation

# Input string from user
text = input("Enter a string: ")

# Remove punctuation
no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct += char

# Output result
print("String without punctuation:", no_punct)
