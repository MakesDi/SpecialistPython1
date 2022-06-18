# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(xa, ya, xb, yb, xc, yc):
    if ((xb-xa)**2+(yb-ya)**2)**0.5 >= ((xc-xb)**2+(yc-yb)**2)**0.5:
        if ((xc-xb)**2+(yc-yb)**2)**0.5 >= ((xc-xa)**2+(yc-ya)**2)**0.5:
            return "AC"
        else:
            return "BC"
    elif ((xb-xa)**2+(yb-ya)**2)**0.5 >= ((xc-xa)**2+(yc-ya)**2)**0.5:
        return "AC"
    else:
        return "AB"

xa = int(input("Введите координаты точки xa: "))
ya = int(input("Введите координаты точки ya: "))
xb = int(input("Введите координаты точки xb: "))
yb = int(input("Введите координаты точки yb: "))
xc = int(input("Введите координаты точки xc: "))
yc = int(input("Введите координаты точки yc: "))

# TODO: your code here
print("Самый короткий отрезок:", distance(xa, ya, xb ,yb, xc, yc))
