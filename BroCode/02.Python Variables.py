# VARIABLE = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

#String = A string is a series of characters. They don't include numbers.

first_name = "Mainak"
food = "pizza"
email = "mainak@xyz.com"

print(first_name) #in this case it prints "Mainak"

print("first_name") #in this case it print the word "first_name"

# f-string

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")


#Integers = A integer is a whole number. Example somebody's age. Integers should'nt be with in qoutes.

age = 20
print(f"You are {age} years old!")


#float = Float contains a decimal point. Example price of any thing.

price = 10.99
print(f"Price of the book is {price}")


#boolen = It will be either True or False

is_student = True
print(f"Are you a student: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")
