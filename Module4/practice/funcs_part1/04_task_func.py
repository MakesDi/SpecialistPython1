# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    return ((x1-x3) * (y2-y3)) - ((x2-x3) * (y1-y3)) != 0 # Две площади треугольника по координатам

x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))
x3 = int(input("x3:"))
y3 = int(input("y3:"))

print(can_triangle(x1, y1, x2, y2, x3, y3))
