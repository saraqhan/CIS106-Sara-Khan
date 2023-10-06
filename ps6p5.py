lname = input("Enter the employee last name: ")
sal = float(input("Enter the employee salary: "))
joblvl = int(input("Enter the employee job level: "))

if joblvl >= 10:
  bnsrt = 0.25
elif 5 <= joblvl <= 9:
  bnsrt = 0.20
else:
  bnsrt = 0.10

bns = sal * bnsrt

print(f"Employee Last Name: {lname}")
print(f"Bonus: ${bns: .2f}")