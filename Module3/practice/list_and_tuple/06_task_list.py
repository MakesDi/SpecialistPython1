# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите второе число: "))    # Второе число

i = 0
list_num = []

while first_number + i < second_number:
    if (first_number + i) % 3 == 0:
        list_num.append(first_number + i)
    i +=1
print("Список всех чисел кратных трем:", list_num)
