from typing import Dict, List

import pandas as pd


def read_transact_csv(file_path: str) -> list:
    if file_path.endswith(".csv"):
        """
        read_transact_csv возвращает список со словарями
        """
        df = pd.read_csv(file_path, encoding="utf-8")
        transactions_list = df.to_dict(orient="records")
        return transactions_list
    else:
        print("Неверный формат файла CSV.")
        return []


def read_transact_xlsx(file_path: str) -> List[Dict]:
    """
   Получение данных об операциях из XLSX-файла.
    """
    opera_1 = pd.read_excel(file_path)
    return opera_1.to_dict("records")


""" Пример использования функции:
#operations = read_transac_xlsx("data/transact_excel.xlsx")
#print(operations)"""
