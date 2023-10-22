
def calc_mpg(miles, gallons):
    if gallons == 0:
        return 0
    else:
        return miles/gallons

trips = []
count = 0

while True:
    destcity = input("Enter destination city (or press Ctrl+Z to stop): ")
    if destcity == '':
        break

    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = calc_mpg(miles, gallons)
    trips.append((destcity, miles, mpg))
    count += 1

print("\nTrip Data:")
for trip in trips:
    destination, miles, mpg = trip
    print(f"Destination City: {destcity}, Miles: {miles}, MPG: {mpg:.2f}")

print(f"Total number of trips entered: {count}")
