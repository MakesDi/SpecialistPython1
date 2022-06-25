# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]

a = int(input("Введите a: "))
b = int(input("Введите b: "))
count = 0

while a <= b:
    if palindrome(a) == True:
        count += 1
    a += 1

print("Полиндромов между a и b:", count)
