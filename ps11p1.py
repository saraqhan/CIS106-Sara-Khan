def discount(qty, price, discrate):
  discamt = (qty * price) * (discrate / 100)
  discprice = (qty * price) - discamt
  return discamt, discprice

def main():
  qty = int(input("Enter the qty: "))
  price = float(input("Enter the price: "))
  discrate = float(input("Enter the discount rate: "))

  discamt, discprice = discount(qty, price, discrate)

  print("This is your discount amount $", discamt)
  print("This is your discounted price $", discprice)
  print("This is your quantity: ", qty)
  print("This is your price: ", price)