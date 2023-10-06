numofbooks = (int(input("Enter the number of books to order: ")))
cpb = float(input("Enter the cost per book: "))

total = numofbooks * cpb

shipping = 0

if total <= 50.00:
  shipping = 25.00

print(f"Your total is: ${total: .2f}")
print(f"Cost of Shipping: ${shipping: .2f}")