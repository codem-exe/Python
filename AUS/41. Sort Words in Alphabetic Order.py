# 41. Python Program to Sort Words in Alphabetic Order
# Take input from user
text = input("Enter a sentence: ")

# Split the sentence into words
words = text.split()

# Sort the list of words
words.sort()

# Display the sorted words
print("\nWords in alphabetical order:")
for word in words:
    print(word)
