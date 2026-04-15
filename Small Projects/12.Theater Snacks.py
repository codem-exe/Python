#Movie Theater Menu



menu = {
    "Popcorn"                 : 200,
    "Cold Drink"              : 120,
    "Nachos"                  : 250,
    "Samosa"                  : 100,
    "Veg Puff"                : 80,
    "Veg Roll"                : 180,
    "Chicken Roll"            : 200,
    "French Fries"            : 150,
    "Ice Cream Cup"           : 90,
    "Chocolate Bar"           : 70,
    "Water Bottle"            : 40
}

cart = []
total = 0

print("------------Menu-------------")
for key, value in menu.items():
    print(f"{key:20}: ₹ {value:.2f}")
print("-----------------------------")

while True:
    food = input("Select an item (q to Quit): ")
    if food == "q" or food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found. Please try again.")

for food in cart:
    total += menu.get(food)


print("-----------------------------")
print("Your Cart contains:")
for item in cart:
    print(f"{item:20}: ₹ {menu[item]:.2f}")
    total += menu[item]
print("-----------------------------")
print(f"Total ₹ {total:.2f}")

print(f"\nTotal Amount: ₹ {total:.2f}")