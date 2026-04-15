# main.py
from data_handler import load_data, save_data
from operations import (
    add_operation,
    show_balance,
    show_all_operations,
    show_categories,
    delete_operation,
    search_operations
)


def main():
    print("Добро пожаловать в Менеджер личных финансов!\n")


    # Загружаем данные при запуске
    data = load_data()

    while True:
        print("=" * 50)
        print("Главное меню:")
        print("1. Добавить операцию (доход / расход)")
        print("2. Посмотреть баланс")
        print("3. Показать все операции")
        print("4. Статистика по категориям")
        print("5. Поиск операций")
        print("6. Удалить операцию")
        print("7. Выйти")
        print("=" * 50)

        choice = input("\nВыберите действие (1-7): ").strip()

        if choice == "1":
            add_operation(data)
        elif choice == "2":
            show_balance(data)
        elif choice == "3":
            show_all_operations(data)
        elif choice == "4":
            show_categories(data)
        elif choice == "5":
            search_operations(data)
        elif choice == "6":
            delete_operation(data)
        elif choice == "7":
            print("\nДо свидания! Данные успешно сохранены.")
            save_data(data) # Финальное сохранение при выходе
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")


if __name__ == "__main__":
    main()