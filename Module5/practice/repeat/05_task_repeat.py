# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    import math
    if (num_items  - (num_items // items_on_page) * items_on_page) == 0:
        return items_on_page
    return num_items  - (num_items // items_on_page) * items_on_page

num_items = int(input("Введите количество наименований товара: "))
items_on_page = int(input("Сколько наименований товара помещается на странице?: "))
print("Число объектов на последней странице:", pagination(num_items, items_on_page), "шт.")
