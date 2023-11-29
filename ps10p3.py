def carprice(msrp, make, model, evhcode):
  tax = 0.07
discp = 0.02 if evhcode == "Y" else 0

msrps = msrp * (1 - discp)
ttl = msrps * (1 + tax)

return ttl

def calcsales(make, model, msrp, ttl):
  sales = {
    "make": make,
    "model": model,
    "msrp": msrp,
    "ttl": ttl
  }

  return sales

def print():
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  msrp = float(input("Enter the msrp of the car: "))
  evhcode = input(Is the car electric (Y or N)?")
  
  ttl = carprice (msrp, make, model, evcode)
  sales = calcsales(make, model, msrp, ttl)
  return sales

while True
  print("Do you want to calculate car price? (Yes or No)?")
 response = input().lower()
if response == 'yes':
  sales = calcsales()
  print("The total is, sales["make"], "is", sales["model"], "is", sales[ttl]")
  else response == 'no'