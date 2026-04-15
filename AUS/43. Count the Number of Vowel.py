# 43. Python Program to Count the Number of Each Vowel

def count_vowels(text):
    vowels = "aeiou"
    count = {vowel: 0 for vowel in vowels}  # Dictionary to hold count of each vowel

    # Loop through the string and count vowels
    for char in text.lower():
        if char in vowels:
            count[char] += 1

    return count

# Input from user
text = input("Enter a string: ")

# Get the vowel counts
vowel_counts = count_vowels(text)

# Display the counts
print("\nVowel counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
