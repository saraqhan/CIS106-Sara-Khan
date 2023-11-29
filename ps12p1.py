def displayarrays(lname):
  for name in lname:
      print(name)

def rdisplay(name):
  for name in reversed(lname):
      print(name)

lname = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

print("Original Order:")
displayarrays(lname)

print("\nReverse Order:")
rdisplay(lname)
