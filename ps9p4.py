def detpayrate(jobcode):
    if jobcode == 'L':
        return 25.0
    elif jobcode == 'A':
        return 30.0
    elif jobcode == 'J':
        return 50.0
    else:
        return 0.0 
      
def calcgrosspay(hours, payrate):
    if hours <= 40:
        return hours * payrate
    else:
        othours = hours - 40
        return (40 * payrate) + (othours * 1.5 * payrate)

employees = []
ttlgp = 0

while True:
    lname = input("Enter last name (or press Ctrl+Z to stop): ")
    if lname == '':
        break

    jobcode = input("Enter job code (L, A, J): ")
    hoursworked = float(input("Enter hours worked: "))

    payrate = detpayrate(jobcode)
    grosspay = calcgrosspay(hoursworked, payrate)
    ttlgp += grosspay

    employees.append((lname, grosspay))

print("\nEmployee Data:")
for employee in employees:
    lname, grosspay = employee
    print(f"Last Name: {lname}, Gross Pay: ${grosspay:.2f}")

print(f"Total of all gross pay: ${ttlgp:.2f}")
