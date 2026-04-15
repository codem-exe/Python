item = input("What item would you like to buy? ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the items: "))

total = price * quantity

print(f"You have bought {item} * {quantity}")
print(f"Your total bill is ${total}")