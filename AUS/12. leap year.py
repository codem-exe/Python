# Python Program to Check Leap Year

year = int (input("Enter the year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("The YEAR is a Leap Year")
else:
    print("It is not a Leap Year")