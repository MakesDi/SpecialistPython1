# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    return int(str(ticket_number)[0:1:1]) + int(str(ticket_number)[1:2:1]) == int(str(ticket_number)[4:5:1]) + int(str(ticket_number)[5:6:1])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
