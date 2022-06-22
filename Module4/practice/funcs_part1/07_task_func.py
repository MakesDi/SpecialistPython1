# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def sec_to_hhmmss (sec_ammount):
    hh = sec_ammount // 3600 
    mm = (sec_ammount - 3600 * hh) // 60
    ss = sec_ammount - 3600 * hh - 60 * mm
    
    if hh < 10:
        hh = "0" + str(hh)
    if mm < 10:
        mm = "0" + str(mm)
    if ss < 10:
        ss = "0" + str(ss)

    return (f"{hh}:{mm}:{ss}")

sec_ammount = int(input("Введите количество секунд: "))

print(sec_to_hhmmss(sec_ammount))
