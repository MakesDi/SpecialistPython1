# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input("Введите число случайных элемнтов n: "))
numbers = []
summa = 0

for i in range(n):
    numbers.append(random.randint(-10,10))
    summa += numbers[i]

print (numbers)
print("Сумма всех элементов:", summa)
