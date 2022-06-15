# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

names_list = input("Введите имена людей: ").split()

i = 0
max_len = 0

while i < len(names_list):
    if max_len < len(names_list[i]):
        max_len = len(names_list[i])
        max_name = names_list[i]
    i += 1
print (max_name)
