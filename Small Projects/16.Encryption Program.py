import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"keys : {key}")

#ENCRYPTION:

plain_text = input("Enter the message to encrypt: ")
encrypt_text = " "

for letter in plain_text:
    index = chars.index(letter)
    encrypt_text += key[index]

print(f"Original Message     : {plain_text}")
print(f"Encrypted Message   : {encrypt_text}")

#DECRYPTION:

encrypt_text = input("Enter the message to decrypt: ")
plain_text = " "

for letter in encrypt_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message   : {encrypt_text}")
print(f"Original Message     : {plain_text}")

