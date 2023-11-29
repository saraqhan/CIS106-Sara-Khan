while True:
  try:
      length = float(input("Enter length: "))
      width = float(input("Enter width: "))
      height = float(input("Enter height: "))
      sqft = 2 * length * width + 2 * length * height + 2 * width * height
      gallons = sqft / 50
      print("You need", gallons, "gallons of paint.")
  except:
      print("Please enter valid numeric values for length, width, and height.")
      break
