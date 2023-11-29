def calcav(county, marketval):
  if county == 'Cook':
      avp = 0.90
  elif county == 'DuPage':
      avp = 0.80
  elif county == 'McHenry':
      avp = 0.75
  elif county == 'Kane':
      avp = 0.60
  else:
      avp = 0.70

  assessedval = marketval* avp
  return assessedval

def sumav():
  ttlav = 0
  ttlmv = 0

  while True:
      print("\nDo you want to calculate the assessed value of a home? (Yes or No)")
      response = input().lower()

      if response == 'yes':
          county = input("Enter the county: ")
          marketval = float(input("Enter the market value: "))
          assessedval = calcav(county, marketval)
          ttlav += assessedval
          ttlmv += marketval
          print("The assessed value is $", assessedval, ".")
      elif response == 'no':
          break
      else:
          print("Enter Yes or No.")

  return ttlav, ttlmv

def main():
  ttlav, ttlmv = sumav()
  print("\nThe total assessed value of all homes is $", ttlav, ".")
  print("The total market value of all homes is $", ttlmv, ".")