student = input("Enter the student data: ").split(", ")

for i in range(0, len(student), 3):
    name, age, note = student[i], int(student[i + 1]), float(student[i + 2])
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Note: {note}\n")
