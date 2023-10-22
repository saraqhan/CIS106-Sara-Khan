def calctuition(credhours, distcode):
    if distcode == 'I':
        return 250 * credhours
    elif distcode == 'O':
        return 550 * credhours
    else:
        return 0  

students = []
ttltuition = 0

while True:
    lname = input("Enter student's last name (or press Ctrl+Z to stop): ")
    if lname == '':
        break

    credhours = int(input("Enter credit hours: "))
    distcode = input("Enter district code (I for in-district, O for out-of-district): ")

    tuitionowed = calctuition(credhours, distcode)
    ttltuition += tuitionowed

    students.append((lname, tuitionowed))

print("\nStudent Data:")
for student in students:
    last_name, tuition_owed = student
    print(f"Last Name: {lname}, Tuition Owed: ${tuitionowed:.2f}")

print(f"Total tuition owed: ${ttltuition:.2f}")
