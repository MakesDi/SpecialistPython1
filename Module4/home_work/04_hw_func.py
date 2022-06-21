# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import math

first_comp = []
second_comp = []

broken_num = input("Введите выражение в формате n x/y, где n - целая часть, x - числитель, у - знаменатель: ")

first_comp = broken_num[0:int(broken_num.find(" - ") + broken_num.find(" + ")+1)]
second_comp = broken_num[int(broken_num.find(" - ") + broken_num.find(" + ")+4):len(broken_num)]

if first_comp.find("/") > 0 and first_comp.find(" ") > 0:
    first_comp_numerator = int(first_comp[0:first_comp.find(" ")])*int(first_comp[first_comp.find("/")+1:len(first_comp)]) + int(first_comp[first_comp.find(" "):first_comp.find("/")])*round(int(first_comp[0:first_comp.find(" ")])/abs(int(first_comp[0:first_comp.find(" ")])))
    first_comp_denominator = int(first_comp[first_comp.find("/")+1:len(first_comp)])
elif first_comp.find("/") > 0:
    first_comp_numerator = int(first_comp[0:first_comp.find("/")])
    first_comp_denominator = int(first_comp[first_comp.find("/")+1:len(first_comp)])
elif first_comp.find("/") < 0 and first_comp.find(" ") < 0: 
    first_comp_numerator = int(first_comp)*round(abs(int(first_comp)))
    first_comp_denominator = round(abs(int(first_comp)))

if second_comp.find("/") > 0 and second_comp.find(" ") > 0:
    second_comp_numerator = int(second_comp[0:second_comp.find(" ")])*int(second_comp[second_comp.find("/")+1:len(second_comp)]) + int(second_comp[second_comp.find(" "):second_comp.find("/")])*round(int(second_comp[0:second_comp.find(" ")])/abs(int(second_comp[0:second_comp.find(" ")])))
    second_comp_denominator = int(second_comp[second_comp.find("/")+1:len(second_comp)])
elif second_comp.find("/") > 0:
    second_comp_numerator = int(second_comp[0:second_comp.find("/")])
    second_comp_denominator = int(second_comp[second_comp.find("/")+1:len(second_comp)])
elif second_comp.find("/") < 0 and second_comp.find(" ") < 0:
    second_comp_numerator = int(second_comp)*round(abs(int(second_comp)))
    second_comp_denominator = round(abs(int(second_comp)))

comm_denom = (first_comp_denominator * second_comp_denominator) // math.gcd(first_comp_denominator, second_comp_denominator)

new_first_numerator = int(first_comp_numerator * comm_denom / first_comp_denominator)
new_second_numerator = int(second_comp_numerator * comm_denom / second_comp_denominator)

if broken_num.find(" - ") > 0:
    res_numerator = new_first_numerator - new_second_numerator
elif broken_num.find(" + ") > 0:
    res_numerator = new_first_numerator + new_second_numerator

ratio = math.gcd(res_numerator, comm_denom)

if res_numerator < 0:
    modified_numerator = int(abs(res_numerator) / ratio)
    minus_sign = "-"
else:
    modified_numerator = int(res_numerator / ratio)
    minus_sign = ""

modified_denominator = int(comm_denom / ratio)

final_floor = int(modified_numerator // modified_denominator)

final_numerator = int(modified_numerator) - final_floor * modified_denominator

if final_floor == 0 and final_numerator == 0:
    print("Ответ: 0")
elif final_floor == 0:
    print(f"Ответ: {minus_sign}{final_numerator}/{modified_denominator}")
elif final_numerator == 0:
    print(f"Ответ: {minus_sign}{final_floor}")
else:
    print(f"Ответ: {minus_sign}{final_floor} {final_numerator}/{modified_denominator}")
