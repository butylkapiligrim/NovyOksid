import re
from pathlib import Path
from typing import Dict, List, Any

from src.csv_xlsx import read_transact_csv, read_transact_xlsx
from src.dictionar_handler import search_transact
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file, sum_amount
from src.widget import convert_date_format, mask_number


def choose_file_format() -> tuple[List[Dict], str]:
    """Запрашивает у пользователя формат файла и возвращает данные транзакций и тип файла.

    Returns:
        tuple Список словарей с транзакциями и тип файла (json, csv, excel).
    """
    print("Добро пожаловать в программу работы с банковскими транзакциями!")
    file = input("""Выберите формат файла: 1. Json 2. CSV 3. Excel\n""")
    if file == "1":
        print("Для обработки выбран json файл.\n")
        return read_json_file(Path("data/operations.json")), "json"
    elif file == "2":
        print("Для обработки выбран csv файл.\n")
        return read_transact_csv("data/transactions.csv"), "csv"
    elif file == "3":
        print("Для обработки выбран excel файл.\n")
        return read_transact_xlsx("data/transactions_excel.xlsx"), "excel"
    else:
        """Если выбрал не от 1 до 3 возращает обратно к началу работы программы """
        print("Пожалуйста, выберите правильный номер опции.")
        return choose_file_format()


def filter_by_status(data: List[Dict]) -> List[Dict]:
    """Фильтрует список транзакций по заданному статусу.

    Args:
        data Список словарей с транзакциями.

    Returns Отфильтрованный список транзакций.
    """
    print("Выберите статус, по которому необходимо выполнить фильтрацию.")
    status = input("Доступные для сортировки статусы: EXECUTED, CANCELED, PENDING\n")

    if status.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        """Если выбрал некорректный статус возращает обратно к вопросу status"""
        print("Некорректный статус, повторите ввод.")
        return filter_by_status(data)

    return filter_by_state(data, status)


def sort_by_date_and_currency(data: List[Dict], file_type: str) -> list[dict[Any, Any]]:
    """Сортирует список транзакций по дате и фильтрует по валюте.

    Args:
        data Список словарей с транзакциями.
        file_type Тип файла (json, csv, excel).

    Returns Отсортированный и отфильтрованный список транзакций.
    """
    to_sort = input("Отсортировать операции по дате? Да/нет \n")
    if to_sort.lower() == "да":
        time = input("По возрастанию или по убыванию?\n")
        if time.lower() == "по возрастанию":
            data = sort_by_date(data)
        elif time.lower() == "по убыванию":
            data = sort_by_date(data, "decreasing")
        else:
            """Если выбрал некорректное значение возращает обратно к вопросу to_sort"""
            print("Некорректное значение, повторите ввод.")
            return sort_by_date_and_currency(data, file_type)
    elif to_sort.lower() == "нет":
        pass
    else:
        print("Некорректный ответ, повторите ввод.")
        return sort_by_date_and_currency(data, file_type)

    to_sort = input("Выводить только рублевые транзакции? Да/нет \n")
    if to_sort.lower() == "да":
        return filter_by_currency(data, "RUB")
    elif to_sort.lower() == "нет":
        return data
    else:
        """Если выбрал некорректный ответ возращает обратно к вопросу to_sort"""
        print("Некорректный ответ, повторите ввод.")
        return sort_by_date_and_currency(data, file_type)


def filter_by_keyword(data: List[Dict]) -> List[Dict]:
    """Фильтрует список транзакций по ключевому слову в описании.

    Args:
        data Список словарей с транзакциями.

    Returns Отфильтрованный список транзакций.
    """
    keyword = input("Введите ключевое слово для фильтрации описаний операций:\n")
    return search_transact(data, keyword)


def main():
    """
    Основная функция, запускающая работу программы.
    """
    data, file_type = choose_file_format()

    to_sort = input("Сортировать операции по статусу? Да/нет \n")
    if to_sort.lower() == "да":
        data = filter_by_status(data)
    elif to_sort.lower() == "нет":
        pass
    else:
        """Если выбрал некорректный ответ возращает обратно к вопросу to_sort"""
        print("Некорректный ответ, повторите ввод.")
        return main()

    data = sort_by_date_and_currency(data, file_type)
    data = filter_by_keyword(data)

    if file_type == "json":
        for item in data:
            print(
                f"Дата: {convert_date_format(item['date'])} | "
                f"Описание: {item['description']} | "
                f"Сумма: {mask_number(item['operationAmount']['amount'])} "
                f"{item['operationAmount']['currency']['name']} | "
                f"Статус: {item['state']}"
            )
        print(f"Сумма транзакций: {sum_amount(data)}")
    elif file_type in ("csv", "excel"):
        for item in data:
            print(
                f"Дата: {convert_date_format(item['date'])} | "
                f"Описание: {item['description']} | "
                f"Сумма: {mask_number(item['amount'])} "
                f"{item['currency']} | "
                f"Статус: {item['state']}"
            )
        print(f"Сумма транзакций: {sum_amount(data)}")
    else:
        print("Некорректный тип файла.")


if __name__ == "__main__":
    main()
