#Validate User Input Exercise:
#1.Username is no more than 12 characters
#2.Username must not contain spaces
#3.Username must not contain digits


username = input("Enter a Username: ")

length = len(username)

spaces = username.count(" ")

alphabet = username.isalpha()

if length <= 12 and spaces == 0 and alphabet is True:
    print("You have sucessfully created your username")
else:
    (print("Invalid Username! TRY AGAIN"))