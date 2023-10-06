prnpl = float(input("Enter the principal amount of a CD: "))
ytm = int(input("Enter the years to maturity of a CD: "))

if prnpl > 100000:
  intrt = 0.06
elif 50000 <= prnpl <= 100000:
  if ytm == 10:
    intrt = 0.05
  elif ytm == 5:
    intrt = 0.04
  else:
    intrt = 0.02
else:
  intrt = 0.02

fyint = prnpl * intrt

print(f"Principal Amount: ${prnpl: .2f}")
print(f"Interest Rate: {intrt * 100}%")
print(f"First Year Interest: ${fyint: .2f}")