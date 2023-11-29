def average(scores, handicap):
  
  avgscore = sum(scores) / len(scores)

  avghandicaps = avgscore + handicap

  return avgscore, avghandicaps

def main():
  lname = input("Enter bowler's last name: ")

  scores = []
  for i in range(3):
      score = float(input(f"Enter score for game {i + 1}: "))
      scores.append(score)

  handicap = float(input("Enter handicap: "))

  avgscore, avghandicaps = average(scores, handicap)

  print("\nBowler Information:")
  print(f"Last Name: {lname}")
  print(f"Average Score: {avgscore:.2f}")
  print(f"Average Score with Handicap: {avghandicaps:.2f}")

main()
