item = input("Enter item: ")
qty = int(input("Enter quantity: "))

A = float(10.00)
B = float(20.00)

if item == "A":
  unitprc = 10.00
else:
  unitprc = 20.00

extprc = qty * unitprc

print(f"Item: {item}")
print(f"Unit Price: ${unitprc: .2f}")
print(f"Extended Price: ${extprc: .2f}")