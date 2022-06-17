# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
brands = []
brands_counter = []
brands_list= []
max_price = 0
posh_brands = []
max_brands =[]

i = 0
j = 0
k = 0
l = 0
m = 0

while i < len(items):
    brands.append(items[i]["brand"])
    i +=1
print ("Товары на складе представлены брэндами:",", ".join(set(brands)))


brands_list.extend(set(brands))

while l < len(brands_list):
    brands_counter.append(brands.count(brands_list[l]))
    l +=1
while m < len(brands_list):
    if brands_counter[m] == max(brands_counter):
        max_brands.append(brands_list[m])
    m +=1
print("На складе больше всего товаров брэнда(ов):",", ".join(set( max_brands)))


while j < len(items):
    if max_price < items[j]["price"]:
        max_price = items[j]["price"]
    j += 1
while k < len(items):
    if items[k]["price"] == max_price:
        posh_brands.append(items[k]["brand"])
    k +=1
print ("На складе самый дорогой товар брэнда(ов):",", ".join(set(posh_brands)))
