def forecast(month, sales):
  forecastpercent = {
      "jan": 0.10, "feb": 0.10, "mar": 0.10,
      "apr": 0.15, "may": 0.15, "jun": 0.15,
      "july": 0.20, "aug": 0.20, "sep": 0.20,
      "oct": 0.25, "nov": 0.25, "dec": 0.25
  }
  nxtmnthsales = sales * (1 + forecastpercent[month])
  return nxtmnthsales

while True:
  response = input("Enter last name, month, and sales? (Yes or No): ")
  if response.lower() == "yes":
      lname = input("Enter last name: ")
      month = input("Enter month: ")
      sales = float(input("Enter sales: "))
      nxtmnthsales = forecast(month, sales)
      print(f"The next month's forecast for {lname} is ${nxtmnthsales:.2f}.")
