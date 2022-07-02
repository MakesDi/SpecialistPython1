## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

```python
with open("workers.txt", "r", encoding="UTF-8") as f:
    workers_str = []
    for line in f:
        workers_str += line.split()
with open("hours_of.txt", "r", encoding="UTF-8") as f:
    true_hours = []
    for line in f:
        true_hours += line.split()
names_in_norm = []
surnames_in_norm = []
salary = []
norm_hours = []
names_in_fact = []
surnames_in_fact = []
fact_hours = []
fact_salary = []
fact_salary_normview = []

i = 5
j = 6
k = 7
l = 9
m = 4
p = 5
h = 6
surname_in_fact = 0

while i < len(workers_str):
    names_in_norm.append(workers_str[i])
    i += 5

while j < len(workers_str):
    surnames_in_norm.append(workers_str[j])
    j += 5

while k < len(workers_str):
    salary.append(int(workers_str[k]))
    k += 5

while l < len(workers_str):
    norm_hours.append(int(workers_str[l]))
    l += 5

while m < len(true_hours):
    names_in_fact.append(true_hours[m])
    m += 3

while p < len(true_hours):
    surnames_in_fact.append(true_hours[p])
    p += 3

while h < len(true_hours):
    fact_hours.append(int(true_hours[h]))
    h += 3

for surname_in_norm in range(len(surnames_in_norm)):
    for surname_in_fact in range(len(surnames_in_fact)):
        if surnames_in_norm[surname_in_norm] == surnames_in_fact[surname_in_fact]:
            if norm_hours[surname_in_norm] >= fact_hours[surname_in_fact]:
                fact_salary.append(round(salary[surname_in_norm] * (fact_hours[surname_in_fact] / norm_hours[surname_in_norm]), 2))
            else:
                fact_salary.append(round(salary[surname_in_norm] + 2 * salary[surname_in_norm] * (fact_hours[surname_in_fact] / norm_hours[surname_in_norm] - 1), 2))

for salary in range(len(fact_salary)):
    if fact_salary[salary] - round(fact_salary[salary], 0) == 0:
        fact_salary_normview.append(int(fact_salary[salary]))
    else:
        fact_salary_normview.append(float(fact_salary[salary]))

for surname_in_norm in range(len(surnames_in_norm)):
    print(f"{names_in_norm[surname_in_norm]} {surnames_in_norm[surname_in_norm]} {fact_salary_normview[surname_in_norm]}")

```

---
