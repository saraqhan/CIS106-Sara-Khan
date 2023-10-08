ttlgp = 0
empcount = 0
response = input("Do you want to continue? (Yes or No): ")
while response == "yes":
  lname = input("Enter employee last name: ")
  hours = float(input("Enter hours worked: "))
  rate = float(input("Enter pay rate: "))
  
if hours > 40:
    regpay = 40 * rate
    otpay = (hours - 40) * (rate * 1.5)
    grosspay = regpay + otpay
else:
    grosspay = hours * rate
    
print(f"Employee Last Name: {lname}")
print(f"Gross Pay: ${grosspay: .2f}")
ttlgp += grosspay
empcount += 1
response = input("Do you want to continue? Yes or NO: ")
if empcount > 0:
  regpay = ttlgp / empcount
  print(f"\nTotal Gross Pay: ${ttlgp:.2f}")
  print(f"Number of Employees: {empcount}")
  print(f"Average Pay: ${regpay:.2f}")