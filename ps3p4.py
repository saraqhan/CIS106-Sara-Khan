make = input("Enter the make: ")
model = input("Enter the model: ")
msrpamt = float(input("Enter the MSRP amount: "))
discper = float(input("Enter the discount percent: "))

amtoff = msrpamt * discper
discprc = msrpamt - amtoff

print(f"Make: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrpamt}")
print(f"Discount Percent: ${discper * 100: .2f}")
print(f"Amount Off MSRP: ${amtoff: .2f}")
print(f"Discounted Price: ${discprc: .2f}")