## "Улучшенный кассовый аппарат"

### Задание
Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров. \
Файл [data/items_sold.txt](data/items_sold.txt) - продажи всех товаров за день. \
Каждая строка файла - покупка одного покупателя.

Узнайте:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму
4. Сколько различных типов товаров было продано за день

### Формат входных данных

Дан текстовый файл. На каждой строке записана информация о проданных товарах в формате:

**тип_товара:цена**, например **fruits:45.10**

Все проданные товары разделены одним или более пробелами.

### Формат выходных данных

Вывести:
1. Какова общая выручка магазина
2. Какова выручка магазина по каждому типу товаров
3. Какой тип товара был продан на самую большую сумму. Если таких несколько, вывести любой.
4. Сколько различных типов товаров было продано за день

### Решение задачи

```python
with open("items_sold.txt", "r") as f:
    sold_str = []
    prices = []
    revenue = 0
    items = []
    item_sales =[]
    total = 0
    best_sales = 0
    for line in f:
        sold_str += line.rstrip().split()
    for item in range(len(sold_str)):
        prices.append(sold_str[item][sold_str[item].find(":") + 1:])
    for price in range(len(prices)):
        revenue += float(prices[price])
print("Общая выручка магазина:", revenue)

for good in range(len(sold_str)):
        items.append(sold_str[good][:sold_str[good].find(":")])
unique_items = list(set(items))

for good in range(len(unique_items)):
    for item in range(len(sold_str)):
        if unique_items[good] == sold_str[item][:sold_str[item].find(":")]:
            total += float(sold_str[item][sold_str[item].find(":") + 1:])
    item_sales.append(unique_items[good] + ": " + str(round(total,2)))
    total = 0
print("Выручка магазина по каждому типу товаров:", *item_sales)

for item in range(len(item_sales)):
    if float(item_sales[item][item_sales[item].find(":") + 2:]) > best_sales:
        best_sales = float(item_sales[item][item_sales[item].find(":") + 2:])

for item in range(len(item_sales)):
    if float(item_sales[item][item_sales[item].find(":") + 2:]) == best_sales:
        best_sales_item = item_sales[item][:item_sales[item].find(":")]
print("Товар, проданный на самую большую сумму:", best_sales_item)
print("Количество различных типов товаров", len(unique_items))
```

---
