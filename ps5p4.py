name = input("Enter name of appliance: ")
cofapp = float(input("Enter the cost of an appliance: "))

if cofapp > 1000:
  wrnt = 0.10 * cofapp
else:
  wrnt = 0.05 * cofapp

total = cofapp + wrnt

print(f"Appliance Name: {name}")
print(f"Appliance Cost: ${cofapp: .2f}")
print(f"Warranty Cost: {wrnt: .2f}")
print(f"Total Cost: ${total: .2f}")