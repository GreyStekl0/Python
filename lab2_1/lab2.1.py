from typing import List, Union


# Обрабатывает вводимые значения, принимает целое число или строку, в случае ввода неккоректных данных возвращает None
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
        if value.isalpha() and value.isupper() and value in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
            return value
        else:
            print("Строка должна быть большой согласной буквой русского алфавита.")
            return None
    else:
        print("Некорректный тип данных.")
        return None


# Принимает список целых чисел и строк, возвращает максимальное число и ближайшую к концу алфавита букву
def calculator(data_list: List[Union[int, str]]) -> Union[int, str]:
    num = [x for x in data_list if isinstance(x, int)]
    letters = [x for x in data_list if isinstance(x, str)]

    max_num = max(num, key=lambda x: x) if num else None
    last_letter = max(letters, key=lambda x: ord(x)) if letters else None

    return max_num, last_letter


# Декоратор, выводит
# количество нечётных отрицательных чисел,
# буквы с изменённым регистром,
# максимальное число,
# ближайшую к концу алфавита букву
def calculator_decorator(func):
    def wrapper(data_list: List[Union[int, str]]):
        result = func(data_list)

        odd_negative_count = sum(1 for x in data_list if isinstance(x, int) and x < 0 and x % 2 != 0)
        print(f"Количество нечётных отрицательных значений: {odd_negative_count}")

        swap_letters = [x.swapcase() for x in data_list if isinstance(x, str)]
        print(f"Буквы с изменённым регистром: {' '.join(swap_letters)}")

        max_number, last_letter = result
        print(f"Максимальное значение: {max_number}")
        print(f"Ближайшая к концу алфавита буква: {last_letter}")

        return result

    return wrapper


@calculator_decorator
def decorated_calculator(data_list: List[Union[int, str]]):
    return calculator(data_list)

# Основная функция, принимает значения пока пользователь не введет end
def main():
    data_list = []

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

    decorated_calculator(data_list)


if __name__ == "__main__":
    main()
