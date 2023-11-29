def displayarrays(lname, scores):
  for i in range(len(lname)):
      print(f"{lname[i]} - Exam Score: {scores[i]}")

def rdisplay(lname, scores):
  for i in reversed(range(len(lname))):
      print(f"{lname[i]} - Exam Score: {scores[i]}")

lname = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
scores = [85, 90, 78, 92, 88, 75, 80, 95, 89, 93]

print("Original Order:")
displayarrays(lname, scores)

print("\nReverse Order:")
rdisplay(lname, scores)
