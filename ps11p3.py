def comms(sales):
  if sales > 100000:
      commsrate = 0.10
  else:
      commsrate = 0.05

  commission = sales * commsrate
  nyt = sales * 0.05

  return commission, nyt

def main():
  lname = input("Enter the salesperson's last name: ")
  sales = float(input("Enter the sales amount: "))
  return lname, sales

def results(lname, commission, nyt):
  print(f"\nSalesperson: {lname}")
  print(f"Commission: ${commission:.2f}")
  print(f"Next Year's Target: ${nyt:.2f}")


lname, sales = main()
commission, nyt = comms(sales)
results(lname, commission, nyt)
