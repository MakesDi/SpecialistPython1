# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data.txt", "r") as f: #Символ / запрещён в названии файла
    s = 0
    for line in f:
        if line.rstrip().isdigit():
            s += int(line)
print(s)
