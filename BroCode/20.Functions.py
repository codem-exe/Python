#Function: Block of reusable code
#          place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} old!")
    print("Happy birthday to you!")
    print()

happy_birthday("Mainak", 19)
happy_birthday("Swaroopa", 19)


#return = statement used to end a function
#         and send a result back to the caller

a = 10
b = 5
def addition(x,y):
    z = x + y
    return z
def subtraction(x,y):
    z = x - y
    return z
def multiplication(x,y):
    z = x * y
    return z
def division(x,y):
    z = x / y
    return z

print(addition(a,b))
print(subtraction(a,b))
print(multiplication(a,b))
print(division(a,b))


# Exercise

def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("mainak","bhattacharjee")

print(full_name)
