# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    s = 0
    for el in args:
        s += el
    return s/ len(args)

def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list

rand = gen_list(10)
print(rand)
print(average(*rand))
