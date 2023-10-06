qty = int(input("Enter the quantity of widgets: "))

if qty > 10000:
  prc = 10.00
elif 5000 <= qty <= 10000:
  prc = 20.00
else:
  prc = 30.00

extprc = qty * prc
tax = 0.07 * extprc
total = extprc + tax

print(f"Extended Price: ${extprc: .2f}")
print(f"Tax Amount: ${tax: .2f}")
print(f"Total: ${total: .2f}")