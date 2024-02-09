def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Считываем температуру в градусах Фаренгейта из ввода пользователя
fahrenheit_temperature = float(input("Введите температуру в градусах Фаренгейта: "))

# Преобразуем температуру из градусов Фаренгейта в градусы Цельсия, используя функцию
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Выводим эквивалентную температуру в градусах Цельсия
print(f"{fahrenheit_temperature} градусов Фаренгейта равно {celsius_temperature:.2f} градусам Цельсия.")