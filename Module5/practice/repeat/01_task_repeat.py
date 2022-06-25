# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random
    randomize_list = []
    for num in range(size):
        randomize_list.append(random.randint(of,to))
    return randomize_list
print(gen_list(5,-5,10))
