numbers = [45, 22, 89, 10, 66]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    
    if num < min_num:
        min_num = num

print("List:", numbers)
print("Max:", max_num)
print("Min:", min_num)