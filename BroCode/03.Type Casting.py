#Typecasting = The process of converting a value of one data type to another

#Explicit vs Implicit

name = "Mainak"
age = "19"
gpa = 8.1
student = True

#Type Function

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))


#Explicit Typecasting

age = float(age)
print(type(age))

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)
print(type(student))

age = bool(age)
print(age)


#Implicit Typecasting
x = 2
y = 2.0

x = x/y
print(x)