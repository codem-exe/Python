#Logical Operators = Used as condtional statements

#                    and = checks if two or more conditions if True
#                    or  = checks if at least one condtion is True
#                    not = True if condition is False, and vice versa

temp = 25
sunny = True

if temp > 0 and temp < 30:
    print("The Temperature is good")

else:
    print("The Temperature is bad")


if not sunny:
    print("Is is cloudy outside")
else:
    print("It is sunny outside")