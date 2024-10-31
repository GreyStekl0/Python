import sqlite3


# Функция для подключения к базе данных
def connect_db(db_name="video_catalog.db"):
    con = sqlite3.connect(db_name)
    con.execute("PRAGMA foreign_keys = ON;")
    return con


# Функция для вывода списка таблиц
def list_tables(con):
    try:
        cur = con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
        tables = cur.fetchall()

        if tables:
            print("\nСписок таблиц в базе данных:")
            for table in tables:
                print(table[0])
        else:
            print("В базе данных нет таблиц.")
    except sqlite3.Error as e:
        print(f"Ошибка при выводе списка таблиц: {e}")


# Функция для создания таблицы
def create_table(con):
    table_name = input("\nВведите название таблицы: ")
    fields = []

    print("Добавьте поля таблицы (название и тип). Введите 'stop' для завершения.")
    while True:
        field_name = input("Название поля (или 'stop' для завершения): ")
        if field_name.lower() == 'stop':
            break
        field_type = input("Тип поля (INTEGER, REAL, TEXT, BLOB): ").upper()
        if field_type in ["INTEGER", "REAL", "TEXT", "BLOB"]:
            fields.append(f"{field_name} {field_type}")
        else:
            print("Неверный тип данных, попробуйте снова.")

    if fields:
        fields_str = ", ".join(fields)
        try:
            con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({fields_str})")
            con.commit()
            print(f"Таблица '{table_name}' успешно создана.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")
    else:
        print("Не были добавлены поля для таблицы.")


# Функция для добавления одной записи
def add_single_record(con):
    table_name = input("\nВведите название таблицы для добавления записи: ")
    try:
        cur = con.execute(f"PRAGMA table_info({table_name})")
        columns = [info[1] for info in cur.fetchall() if info[1] != 'id']

        values = []
        for col in columns:
            value = input(f"Введите значение для '{col}': ")
            values.append(value)

        placeholders = ", ".join(["?"] * len(columns))
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        con.execute(query, values)
        con.commit()
        print("Запись успешно добавлена.")

    except sqlite3.Error as e:
        print(f"Ошибка при добавлении записи: {e}")


# Функция для добавления нескольких записей
def add_multiple_records(con):
    table_name = input("\nВведите название таблицы для добавления записей: ")
    try:
        cur = con.execute(f"PRAGMA table_info({table_name})")
        columns = [info[1] for info in cur.fetchall() if info[1] != 'id']

        records = []
        print("Введите записи. Введите 'stop' для завершения.")
        while True:
            values = []
            for col in columns:
                value = input(f"Введите значение для '{col}' (или 'stop' для завершения): ")
                if value.lower() == 'stop':
                    break
                values.append(value)
            if values:
                records.append(tuple(values))
            else:
                break

        placeholders = ", ".join(["?"] * len(columns))
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        con.executemany(query, records)
        con.commit()
        print("Записи успешно добавлены.")

    except sqlite3.Error as e:
        print(f"Ошибка при добавлении записей: {e}")


# Функция для вывода всех записей таблицы
def display_records(con):
    try:
        table_name = input("Введите название таблицы для вывода записей: ")
        cur = con.execute(f"SELECT * FROM {table_name}")
        records = cur.fetchall()

        if records:
            column_names = [description[0] for description in cur.description]
            for row in records:
                record = ", ".join(f"{col} = {val}" for col, val in zip(column_names, row))
                print(record)
        else:
            print(f"Таблица '{table_name}' пуста.")
    except sqlite3.Error as e:
        print(f"Ошибка при выводе записей: {e}")


# Функция для отображения меню
def menu():
    print("\n--- Меню ---")
    print("1. Создать таблицу")
    print("2. Добавить одну запись в таблицу")
    print("3. Добавить несколько записей в таблицу")
    print("4. Показать все записи из таблицы")
    print("5. Выход")
    choice = input("Выберите действие (1-5): ")
    return choice


def main():
    con = connect_db()
    print("База данных подключена.")

    while True:
        list_tables(con)
        choice = menu()

        if choice == '1':
            create_table(con)
        elif choice == '2':
            add_single_record(con)
        elif choice == '3':
            add_multiple_records(con)
        elif choice == '4':
            display_records(con)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    con.close()
    print("Соединение с базой данных закрыто.")


if __name__ == "__main__":
    main()
