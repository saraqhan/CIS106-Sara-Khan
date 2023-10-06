fixedcosts = float(input("Enter fixed costs: "))
pppunit = float(input("Enter price per unit: "))
cpu = float(input("Enter cost per unit: "))

brkevenpt = fixedcosts / (pppunit - cpu)

print(f"The break even point is {brkevenpt: .2f}.")