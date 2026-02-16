attendance = ["P", "P", "A", "P", "P"]

present = 0
total = len(attendance)

for day in attendance:
    if day == "P":
        present = present + 1

percentage = (present / total) * 100

print("Attendance Percentage:", percentage)