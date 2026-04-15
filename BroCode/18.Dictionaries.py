# Dictionary = A collection of {key:value} pairs
#              Ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


# print(capitals.get("India"))
#
# capitals.update({"Germany":"Berlin"})
#
# capitals.pop("China")
#
# capitals.popitem()
#
# capitals.clear()

# keys = (capitals.keys())
# print(keys)
#
# values = (capitals.values())
# print(values)

# items = capitals.items()

country = input("Enter the name of a country: ")

if capitals.get(country):

    print(f"The capital of {country} is {capitals[country]}.")
    # print("Data Available")

else:
    print("Data doesn't exist")


# for key, value in capitals.items():
#     print(f"{key}:{value}")