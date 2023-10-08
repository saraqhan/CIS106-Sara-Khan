ttldisc = 0
response = input("Do you want to continue? Yes or No: ")
while response == "yes":
  qty = int(input("Enter quantity of the item: "))
  price = float(input("Enter the price of the item: "))
  extprc = qty * price
  if extprc > 10000.0:
    discper = 0.25 
  else:
   discper = 0.10
  discamt = extprc * discper
  ttl = extprc - discamt
  print(f"Extended Price: ${extprc:.2f}")
  print(f"Discount Amount: ${discamt:.2f}")
  print(f"Total: {ttl:.2f}")
  ttldisc += discamt
  response = input("Do you want to continue? Yes or NO: ")
  print(f"Total Discounts: ${ttldisc:.2f}")