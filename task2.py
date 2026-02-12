marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for i in marks:
    if i >= 50:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("Total students:", len(marks))
print("Passed:", pass_count)
print("Failed:", fail_count)
