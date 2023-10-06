ptnum = input("Enter a part number: ")
qty = int(input("Enter a quantity: "))

if not ptnum.isdigit():
  ptnum = int(ptnum)
if ptnum == 10 or ptnum == 55:
  ucost = 1.00
elif ptnum == 99:
  ucost = 2.00
elif ptnum == 80 or ptnum == 70:
  ucost = 3.00
else:
  ucost = 5.00

total = qty * ucost

print(f"Part Number: {ptnum}")
print(f"Cost Per Unit: ${ucost: .2f}")
print(f"Total: ${total: .2f}")