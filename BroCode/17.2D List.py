
fruits =     ["apple","orange","banana","coconut"]
vegetables = ["cucumber","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats]

# groceries = [["apple","orange","banana","coconut"],
#              ["cucumber","carrots","potatoes"],
#              ["chicken","fish","turkey"]]

print(groceries[1][2])

for collection in groceries:
    # print (collection)
    for food in collection:
        print(food, end=" ")
    print()


