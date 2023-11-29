total = 0
tax = 0

def ttl_tax(qty, uprice):
    global total
    global tax
    total = qty * uprice
    tax = 0.07 * total

def main():
    qty = int(input("Enter quantity of the item: "))
    uprice = float(input("Enter unit price of the item: "))
    ttl_tax(qty, uprice)

    print("\nTransaction Summary:")
    print(f"Quantity: {qty}")
    print(f"Unit Price: ${uprice:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Tax (7% of Total): ${tax:.2f}")

main()
