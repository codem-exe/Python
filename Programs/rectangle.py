#program to find area and perimeter of a rectangle

length = float(input("Enter the Length of the rectangle: "))
breath = float(input("Enter the breath of the rectaangle:"))

area = length * breath
perimeter = 2 * ( length + breath )

print("Area of the rectangle is",area)
print("Perimeter of the rectangle is",perimeter)