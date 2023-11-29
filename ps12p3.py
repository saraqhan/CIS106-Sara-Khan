def displayarrays(lname, scores):
  for i in range(len(lname)):
      print(f"{lname[i]} - Score: {scores[i]}")

def high_low(lname, scores):
  if not lname or not scores:
      print("No data available.")
      return

  highvar = 0
  lowvar = 999
  highindex = 0
  lowindex = 0

  for i in range(len(scores)):
      if scores[i] > highvar:
          highvar = scores[i]
          highindex = i
      if scores[i] < lowvar:
          lowvar = scores[i]
          lowindex = i

  print(f"\nHighest Score: {lname[highindex]} - {highvar}")
  print(f"Lowest Score: {lname[lowindex]} - {lowvar}")
  
with open('data.txt', 'r') as file:
  data = [line.strip().split() for line in file]

lname = [item[0] for item in data]
scores = [int(item[1]) for item in data]

print("All Data:")
displayarrays(lname, scores)

high_low(lname, scores)
