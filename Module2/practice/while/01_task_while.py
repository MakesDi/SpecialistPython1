# Даны два целые числа a и b. Выведите на экран все целые четные числа от a до b включительно.
# Формат входных данных: Дано два целых числа a и b. Гарантируется, что a < b
# Формат выходных данных: Выведите все числа, требуемые по условию задачи.

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

i = a

while i < b + 1:
    if i % 2 ==0:
        print (i)
    i += 1
    
