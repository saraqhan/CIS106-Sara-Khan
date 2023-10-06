pppshr = (float(input( "Enter the purchase price per share: ")))
crntstkprc = (float(input("Enter the current stock price: ")))
qty = (float(input("Enter the quantity of stock: ")))

value = (crntstkprc - pppshr) * qty

if value > 0:
  print(f"You have gained ${value: .2f} from your investment.")
elif value < 0:
  print(f"You have lost ${abs(value): .2f} from your investment.")
else:
  print("Your investment value has not changed.")