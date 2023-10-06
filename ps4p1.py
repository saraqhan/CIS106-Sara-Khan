exam1_score = float(input("Enter score for Exam 1 (out of 100): "))
exam2_score = float(input("Enter score for Exam 2 (out of 100): "))

exam1_weighted = 0.60
exam2_weighted = 0.40
total = (exam1_score * exam1_weighted) + (exam2_score * exam2_weighted)

print(f"Total Score: {total}")