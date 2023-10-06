lname = input("Enter Last Name: ")
numofdep = int(input("Enter Number of Dependants: "))
grossin = float(input("Enter Gross Income: "))

adjgrsin = grossin - (numofdep * 12000)

if adjgrsin > 50000:
  taxrt = 0.20
else:
  taxrt = 0.10

intaxrt = adjgrsin * taxrt

if intaxrt < 0:
  intaxrt = 100

print(f"Last Name: {lname}")
print(f"Gross Income: ${grossin: .2f}")
print(f"Number of Dependants: {numofdep}")
print(f"Adjusted Gross Income: ${adjgrsin: .2f}")
print(f"Income Tax: ${intaxrt: .2f}")