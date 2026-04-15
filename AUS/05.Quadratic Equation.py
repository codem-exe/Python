# Python Program to Solve Quadratic Equation

import cmath

a = float (input("Enter coefficient a: "))
b = float (input("Enter coefficient b: "))
c = float (input("Enter coefficient c: "))

d = a**2 - 4 * b * c

root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print(f"The roots of the equation are: {root1:.5} and {root2:.5}")