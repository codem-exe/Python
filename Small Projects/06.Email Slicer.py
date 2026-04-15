email = input("Enter your E-mail Address: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and doamin is {domain}")