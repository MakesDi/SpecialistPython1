# Напишите функцию находящую n-ое число Фибоначчи.

def fib_num(n):
    fib_str = [0,1]
    for num in range(n-2):
        fib_str.append(sum(fib_str[num:(num+2)]))
    return fib_str[n-1]

n = int(input("Введите число n: "))

print("n-ое число Фибоначчи:", fib_num(n))
