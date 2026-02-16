employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

# assume first employee has highest salary
highest_employee = ""
highest_salary = 0

# check each employee
for name, salary in employees.items():
    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

print("Highest Salary:", highest_employee, "-", highest_salary)