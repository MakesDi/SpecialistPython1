# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

tup_one = 1, -2, 3, 4, -5, 0
tup_two = 7, -9, 0, 1, 2, 3, -5
tup_three = -5, 4, -7, 0, 8, 1

count = 0
tup_cross = []

for num1 in range(len(tup_one)):
    for num2 in range(len(tup_two)):
        if tup_two[num2] == tup_one[num1]:
            tup_cross.append(tup_two[num2])

for num3 in range(len(tup_three)):
    for num4 in range(len(tup_cross)):
        if tup_three[num3] == tup_cross[num4]:
            count += 1
print("Количество элементов, которые встречаются во всех трех кортежах:", count)
