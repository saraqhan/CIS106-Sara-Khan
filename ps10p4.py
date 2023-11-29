def calcttp(mileschi):
  if mileschi >= 30:
      return 12
  elif 20 <= mileschi < 30:
      return 10
  elif 10 <= mileschi < 20:
      return 8
  else:
      return 5

def calcsttp():
  ttl = 0
  while True:
      print("\nDo you want to calculate the ticket price? (Yes or No)")
      response = input().lower()

      if response == 'yes':
          mileschi = float(input("Enter the miles from Chicago: "))
          ticket = calcttp(mileschi)
          ttl += ticket
          print("The ticket price is $", ticket, ".")
      elif response == 'no':
        break
      else:
        print("Enter Yes or No.")
        
      return ttl

def main():
  ttlsttp = calcsttp()
  print("\nThe total price of all the tickets is $", ttlsttp, ".")