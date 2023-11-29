def avg_ttl(scores):
  points = sum(scores)
  avgscore = points / len(scores)
  return points, avgscore

def main():
  lname = input("Enter the student's last name: ")
  examscores = []

  for i in range(3):
      score = float(input(f"Enter exam score {i + 1}: "))
      examscores.append(score)

  return lname, examscores

def results(lname, points, avgscore):
  print(f"Student: {lname}")
  print(f"Total Points: {points}")
  print(f"Average Exam Score: {avgscore:.2f}")

lname, scores = main()
points, avgscore = avg_ttl(scores)
results(lname, points, avgscore)


