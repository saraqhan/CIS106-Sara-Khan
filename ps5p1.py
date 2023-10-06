qty = int(input("Enter quantity: "))

if qty > 1000:
  unitprc = 3.00
else:
  unitprc = 5.00

extprc = qty * unitprc

tax = 0.07 * extprc

total = extprc + tax

print(f"Quantity: {qty}")
print(f"Unit Price: ${unitprc:.2f}")
print(f"Extended Price: ${extprc: .2f}")
print(f"Tax: ${tax: .2f}")
print(f"Total: ${total: .2f}")