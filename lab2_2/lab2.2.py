from typing import List, Union
from math import degrees, pi
from itertools import filterfalse
from time import perf_counter
import mymodule

def input_handler(value: Union[int, str]) -> Union[int, str, None]:
    if value == "":
        print("Введено пустое значение.")
        return None

    if isinstance(value, int):
        if value < 0:
            return value
        else:
            print("Число должно быть отрицательным.")
            return None

    elif isinstance(value, str):
        is_consonant = lambda x: x.isalpha() and x.isupper() and x in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
        result = list(filterfalse(is_consonant, [value]))
        if not result:
            return value
        else:
            print("Строка должна быть большой согласной буквой русского алфавита.")
            return None
    else:
        print("Некорректный тип данных.")
        return None

def calculator(data_list: List[Union[int, str]]) -> Union[int, str]:
    num = [x for x in data_list if isinstance(x, int)]
    letters = [x for x in data_list if isinstance(x, str)]

    max_num = max(num, key=lambda x: x) if num else None
    last_letter = max(letters, key=lambda x: ord(x)) if letters else None

    return max_num, last_letter

def calculator_decorator(func):
    def wrapper(data_list: List[Union[int, str]]):
        start_time = perf_counter()  # Начало замера времени
        result = func(data_list)
        end_time = perf_counter()  # Конец замера времени

        odd_negative_count = sum(1 for x in data_list if isinstance(x, int) and x < 0 and x % 2 != 0)
        print(f"Количество нечётных отрицательных значений: {odd_negative_count}")

        swap_letters = [x.swapcase() for x in data_list if isinstance(x, str)]
        print(f"Буквы с изменённым регистром: {' '.join(swap_letters)}")

        max_number, last_letter = result
        if max_number is not None:
            max_number = degrees(max_number * pi / 2)  # Преобразование числа в градусы с использованием degrees
        print(f"Максимальное значение (в градусах): {max_number}")
        print(f"Ближайшая к концу алфавита буква: {last_letter}")

        print(f"Время выполнения: {end_time - start_time} секунд")  # Вывод времени выполнения

        return result
    return wrapper

@calculator_decorator
def decorated_calculator(data_list: List[Union[int, str]]):
    return calculator(data_list)

def main():
    data_list = []

    generated_numbers = [mymodule.generate_random_1() for _ in range(5)]
    generated_numbers += [mymodule.generate_random_2() for _ in range(5)]
    print("Сгенерированные числа:", generated_numbers)

    while True:
        user_input = input("Введите значение (или 'end' для завершения): ")
        if user_input.lower() == "end":
            break

        try:
            value = int(user_input)
        except ValueError:
            value = user_input

        processed_value = input_handler(value)
        if processed_value is not None:
            data_list.append(processed_value)

    decorated_calculator(data_list + generated_numbers)

if __name__ == "__main__":
    main()
