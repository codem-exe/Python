# name = (input("Enter your full name: "))
name = "Mainak Bhattacharjee"
# phone_no = (input("Enter your phone number: "))
phone_no = "75789-54437"

print(len(name)) #length function

print(name.find("M")) #first occurance

print(name.rfind("j")) #last occurance

print(name.capitalize()) #capitalize the first letter of the sring

print(name.upper()) #makes all the letter uppercase

print(name.lower()) #makes all the letter lowercase

print(name.isdigit()) #checks if the strings contains only digits

print(name.isalpha()) #checks if the strings contains only alphabets

print(phone_no.count("-")) #count the number of different things in the string

print(phone_no.replace("-"," "))
