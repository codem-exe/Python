# Invoice Printing

customer_details ={
                  "Mainak": 1500,
                  "Anuja": 2300,
                  "Anand": 1200,
                  "Swaroopa": 900,
                  "Monjistha": 2000
                  }


def display_invoice(name, due_amount, due_date):
    print(f"Hello {name}!")
    print(f"Your bill of ${due_amount} is due on {due_date}")
    print("Thank You!")

recheck = True

while recheck:

    customer_name = input("Enter your name: ")
    amount = customer_details.get(customer_name)
    pay_by = "30-04-2025"

    if amount is None:
        print("Data Not Available")
    else:
        display_invoice(customer_name,amount,pay_by)

    user_input = input("Want to Re-Check ? (y/n): ")
    user_input = user_input.lower()

    if user_input != "y":
        recheck = False
