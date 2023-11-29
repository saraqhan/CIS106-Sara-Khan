def displayarrays(name, average):
  for i in range(len(name)):
      print(f"{name[i]} - Batting Average: {average[i]}")

def search(ntf, name, average):
  for i in range(len(name)):
      if name[i].lower() == ntf.lower():
          print(f"\nPlayer found:\n{ntf} - Batting Average: {average[i]}")
          return
  print(f"\nName not found: {ntf}")

with open('playerdata.txt', 'r') as file:
  data = [line.strip().split() for line in file]

pname = [item[0] for item in data]
battingavg = [float(item[1]) for item in data]

print("All Player Data:")
displayarrays(pname, battingavg)

while True:
  searchlname = input("\nEnter a last name to search (or 'exit' to quit): ")
  if searchlname.lower() == 'exit':
      break
  search(searchlname, pname, battingavg)
