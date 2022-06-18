# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random

n = int(input("Введите число случайных элемнтов n: "))
numbers = []
summa = 0

for i in range(n):
    numbers.append(random.randint(-10,10))

for j in range(n):
    if numbers[j] > 0:
        summa += numbers[j]

print (numbers)
print("Сумма всех положительных элементов:", summa)
