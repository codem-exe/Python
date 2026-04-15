#Conditional Expression: A one-line shorcut for the if-else statement (ternary operators)
#                        Print or assign one of two values based on a condtion
#                        X if condition else Y
num = 2
a = 6
b = 10
age = 19

temp = 20

user_role = "admin"

print("Positive" if num > 0 else "Negative")


print(f"{num} is an even number" if num %2 == 0 else f"{num} is an odd number")

max_num = a if a > b else b
min_num = a if a < b else b


print(max_num)
print(min_num)

print("Adult" if age >= 18 else "Child")

print ("Hot" if temp > 20 else "Cold")


access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)