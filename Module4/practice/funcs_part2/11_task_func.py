# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(args):
    return sum(args) / len(args)

list_avg = [3, 3, 8, 6, 18]
tup_avg = 1, 2.5, 4, 8, -5

print(average(list_avg))
print(average(tup_avg))
