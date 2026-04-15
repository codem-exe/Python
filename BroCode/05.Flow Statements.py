#if = Do some code only IF some condtion is True
#     Else do something else

age = int(input("Enter your age: "))

if age >= 18 and age:
    if age >= 101:
        print("You are to old to vote.")
    else:
        print("Hey! you are eligible to vote.")

else:
    print("Sorry! you are not old enough to vote.")