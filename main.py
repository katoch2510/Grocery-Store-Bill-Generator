def generate_bill():
    print("========== WELCOME TO KATOCH MART ==========\n")
    items = []
    total = 0

    while True:
        name = input("Enter item name: ")
        quantity = int(input(f"Enter quantity of '{name}': "))
        price = float(input(f"Enter price of '{name}': "))

        amount = quantity * price
        total += amount

        items.append([name, quantity, price, amount])

        more = input("Add more items? (yes/no): ").lower()
        if more != "yes":
            break

    print("\n========== FINAL BILL ==========")
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Amount"))
    print("-" * 50)

    for item in items:
        print("{:<20} {:<10} {:<10} {:<10.2f}".format(item[0], item[1], item[2], item[3]))

    print("-" * 50)
    print("{:<20} {:<10} {:<10} {:<10.2f}".format("", "", "TOTAL:", total))
    print("=============================================")

# Run the bill generator
generate_bill()
