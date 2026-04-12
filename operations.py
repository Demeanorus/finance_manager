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


def show_balance(data: dict) -> None:
    """Показывает текущий баланс."""
    incomes, expenses, balance = calculate_balance(data)

    print("\n=== Текущий баланс ===")
    print(f"Доходы:     +{incomes:,.2f} ₽")
    print(f"Расходы:    -{expenses:,.2f} ₽")
    print(f"Баланс:      {balance:,.2f} ₽")

    if balance > 0:
        print("Отлично! Положительный баланс.")
    elif balance < 0:
        print("Внимание! Ты в минусе.")


def show_all_operations(data: dict) -> None:
    """Выводит все операции (новые сверху)."""
    if not data["operations"]:
        print("\nПока нет операций.")
        return

    print("\n=== Все операции ===")
    print("-" * 85)
    print(f"{'Дата':<18} {'Тип':<8} {'Сумма':<12} {'Категория':<15} Описание")
    print("-" * 85)

    for op in reversed(data["operations"]):
        sign = "+" if op["type"] == "Доход" else "-"
        print(
            f"{op['date']:<18} "
            f"{op['type']:<8} "
            f"{sign}{op['amount']:>9,.2f} ₽ "
            f"{op['category']:<15} "
            f"{op['description']}"
        )





