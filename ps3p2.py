lname = input("Enter last name: ")
midterm = float(input("Enter midterm score: "))
final = float(input("Enter final exam score: "))

total = midterm * 0.4 + final * 0.6

print(f"{lname}, your total exam points are {total:.2f}")