side_a = int(input("Введите длину стороны A: "))
side_b = int(input("Введите длину стороны B: "))
side_c = int(input("Введите длину стороны C: "))
if side_a == side_b or side_b == side_c or side_a == side_c:
    print("YES")
else:
    print("NO")
