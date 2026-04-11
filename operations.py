# operations.py
from datetime import datetime
from collections import defaultdict
from data_handler import save_data


def add_operation(data: dict) -> None:
    """Добавляет новую операцию (доход или расход)."""
    print("\n=== Добавление операции ===")

    # Защита ввода суммы
    while True:
        try:
            amount = float(input("Сумма: "))
            if amount <= 0:
                print("Сумма должна быть больше 0!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите число.")

    # Защита ввода типа
    while True:
        op_type = input("Тип (доход/расход): ").strip().lower()
        if op_type in ["доход", "расход"]:
            break
        print("Введите 'доход' или 'расход'")

    category = input("Категория: ").strip() or "Прочее"
    description = input("Описание (Не обязательно):  ").strip()

    operation = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": "Доход" if op_type == "доход" else "расход",
        "amount": amount,
        "category": category,
        "description": description
    }

    data["operations"].append(operation)
    save_data(data)
    print("Операция успешно добавлена!")


def calculate_balance(data: dict) -> tuple[float, float, float]:
    """Возвращает (доходы, расходы, баланс)."""
    incomes = sum(op["amount"] for op in data["operations"] if op["type"] == "Доход")
    expenses = sum(op["amount"] for op in data["operations"] if op["type"] == "Расход")
    balance = incomes - expenses
    return incomes, expenses, balance



