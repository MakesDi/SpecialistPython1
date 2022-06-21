# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    return (x - xc)**2 + (y - yc)**2 < r**2

x = int(input("x:"))
y = int(input("y:"))
xc = int(input("xc:"))
yc = int(input("yc:"))
r = int(input("r:"))

if point_in_circle(x, y, xc, yc, r) == True:
    print("Точка строго лежит внутри окружности")
else:
    print("Точка не лежит внутри окружности")

# Не забудьте протестировать вашу функцию
