# Главный модуль программы
from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius
)
from length import (
    meters_to_kilometers,
    kilometers_to_meters
)
from weight import (
    kilograms_to_grams,
    grams_to_kilograms
)
def main():
    while True:
        print("\n===== КОНВЕРТЕР ВЕЛИЧИН =====")
        print("1. Преобразование температуры")
        print("2. Преобразование длины")
        print("3. Преобразование массы")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "0":
            print("Программа завершена.")
            break
        if choice not in ["1", "2", "3"]:
            print("Ошибка: выберите пункт от 0 до 3.")
            continue
        try:
            value = float(input("Введите значение: "))
        except ValueError:
            print("Ошибка: необходимо ввести число.")
            continue
        if choice == "1":
            print("1. Цельсий -> Фаренгейт")
            print("2. Фаренгейт -> Цельсий")
            direction = input("Выберите направление: ")
            if direction == "1":
                result = celsius_to_fahrenheit(value)
                print("Результат:", round(result, 2), "°F")
            elif direction == "2":
                result = fahrenheit_to_celsius(value)
                print("Результат:", round(result, 2), "°C")
            else:
                print("Неверное направление.")
        elif choice == "2":
            print("1. Метры -> Километры")
            print("2. Километры -> Метры")
            direction = input("Выберите направление: ")
            if direction == "1":
                result = meters_to_kilometers(value)
                print("Результат:", result, "км")
            elif direction == "2":
                result = kilometers_to_meters(value)
                print("Результат:", result, "м")
            else:
                print("Неверное направление.")
        elif choice == "3":
            print("1. Килограммы -> Граммы")
            print("2. Граммы -> Килограммы")
            direction = input("Выберите направление: ")
            if direction == "1":
                result = kilograms_to_grams(value)
                print("Результат:", result, "г")
            elif direction == "2":
                result = grams_to_kilograms(value)
                print("Результат:", result, "кг")
            else:
                print("Неверное направление.")
if __name__ == "__main__":
    main()
