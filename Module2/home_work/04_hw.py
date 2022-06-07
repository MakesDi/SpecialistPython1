# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######
n = int(input("Введите сторону квадрата 2 < а < 31: "))
k = n - 2
print("","#"*n)
for i in range(k):
    print('#',' '*k, "#")
print("","#"*n)
