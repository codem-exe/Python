# Object = A "bundle" of related attributes (variable) and methods (functions)
#          Ex.: Phone, Cup, Book
#          We need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive (self):
        print(f"You drive a {self.model}")

car1 = Car("Ignis",2022,"Nexa Blue", False)
car2 = Car("BMW X-Series",2025, "Royal Blue", True)

print(car1.model)
print(car1.year)
print(car1.drive())

print(car2.model)
print(car2.year)
print(car2.drive())