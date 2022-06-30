## "Высокооплачиваемые сотрудники"

### Задание
В файле [data/salaries.txt](data/salaries.txt) даны зарплаты сотрудников.

Выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000. \
Формат вывода смотри в "Формат выходных данных"

### Формат входных данных

Дан текстовый файл. \
В первой строке указаны названия параметров сотрудника. \
В каждой следующей строке дана информация о сотруднике.

### Формат выходных данных

Записать информацию в файл highly_paid.txt о сотрудниках с зарплатой выше 60000.

Сотрудников вывести в формате: Фамилия И.О., \
например: **Иванов И.П.** (зарплаты в выходной файл не записывать)

### Решение задачи

```python

salaries_nospaces = []
salaries_ammount = []
surnames = []
names = []
middle_names =[]
i = 4
j = 5
k = 6

with open("salaries.txt", "r", encoding="UTF-8") as f:
    for line in f:
        for salary in range(len(line.split())):
            salaries_nospaces.append(line.split()[salary])

for salary in range(len(salaries_nospaces)):
     if salaries_nospaces[salary].isdigit():
         salaries_ammount.append(int(salaries_nospaces[salary]))

while i < len(salaries_nospaces):
     surnames.append(salaries_nospaces[i])
     i += 4

while j < len(salaries_nospaces):
     names.append(salaries_nospaces[j][0:1:1] + ".")
     j += 4

while k < len(salaries_nospaces):
     middle_names.append(salaries_nospaces[k][0:1:1] + ".")
     k += 4

with open("highly_paid.txt", "w", encoding="UTF-8") as f:
    for big_salary in range(len(salaries_ammount)):
        if salaries_ammount[big_salary] > 60000:
            f.write(surnames[big_salary] + " " + names[big_salary] + middle_names[big_salary] + "\n")
```

---
