# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
def from_meters_to_foots(n):
    return round(0.3048 * n, 2)
dist_foots = list(map(from_meters_to_foots, distances))
print(dist_foots)
