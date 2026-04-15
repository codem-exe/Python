#This program helps us find a data from a dictionary

data = {
    "Mainak": "18748487878",
    "Anand": "18748487879",
    "Anuja": "18748487880",
    "Swaroopa": "18748487881",
    "Monjistha": "18748487882"
}

#If we know the name of the person this function find the registration number
def name_data(x):
    if x in data:
        print(f"The Registration Number of {x} is: {data.get(x)}")
    else:
        print("Data is Not Available")

#If we know the registration number of the person this function find their name
def registration(x):
    found = False
    for key, value in data.items():
        if value == x:
            print(f"The Registration Number: {x} belongs to: {key}")
            found = True
            break
    if not found:
        print("Data is Not Available")

run = True

while run:
    choice = input("Which value do you want Name or Registration Number (Type Exit for Exiting the program): ").lower()

    if choice == "name":
        reg = input("Enter the Registration Number: ")

        if reg.isdigit():
            registration(reg)
        else:
            print("Enter a Valid Registration Number!!")

    elif choice == "registration number":
        name = input("Enter the Name: ").capitalize()

        if name.isalpha():
            name_data(name)
        else:
            print("Please Enter a Valid Name!!")

    elif choice == "exit":
        run = False
        print("Exiting the program!!")

    else:
        print("Enter a Valid Choice!!")