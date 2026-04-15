# *args       = allows you to pass multiple non-key arguments (tuple)
# **kwargs    = allows you to pass multiple keyword-arguments (dictionary)
#             * unpacking operator
#                   1.Positional
#                   2.Default
#                   3.KEYWORD
#           --->    4.Arbitrary


# *args

def add(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(add(1,2,3))


def display_name(*args):
    for arg in args:
        print(arg, end= " ")


display_name("Mrinal","Kanti","Bhattacharjee")
print()



# **kwargs

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street = "Raja Ram Mohan Road",
              city = "Dharmanagar",
              state = "Tripura",
              zip = "799250")

print()


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=", ")

shipping_label("Mrs.","Jayanti","Bhattacharjee",
               Street = "Link Road",
               Sub_Street = "Lane no.10",
               Apartment_Num = "House no.13",
               City = "Silchar",
               State = "Assam",
               Pin = "788006")