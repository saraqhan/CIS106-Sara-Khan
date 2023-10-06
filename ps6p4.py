numoft = int(input("Enter the number of concert tickets: "))

if numoft >= 25:
  ppt = 50.00
elif 10 <= numoft <= 24:
  ppt = 60.00
elif 5 <= numoft <= 9:
  ppt = 75.00
else:
  ppt = 75.00

total = numoft * ppt

print(f"Number of Tickets: {numoft}")
print(f"Price Per Ticket: ${ppt: .2f}")
print(f"Total: ${total:.2f}")