my_expenses: list[float] = []


def add_expense(expenses: list[float], value: float):
    expenses.append(value)
    print("Расход добавлен")


def get_total(expenses: list[float]) -> float:
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    return sum(expenses) / len(expenses)


def delete_expence(expenses: list[float], index: int):
    del expenses[index]
    print("Расход удален")


def print_report(expenses: list[float]):
    print("=" * 30)
    print("Расходы:")
    for i in range(len(expenses)):
        print(f"{i + 1}. {expenses[i]}")
    print("=" * 30)


while True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice = input("\nВыберите пункт меню (1-5): ")
    match choice:
        case "1":
            value = float(input("Введите сумму расхода: "))
            add_expense(my_expenses, value)
        case "2":
            print_report(my_expenses)
        case "3":
            print("Сумма расходов: " + str(get_total(my_expenses)))
            print("Средний расход: " + str(get_average(my_expenses)))
        case "4":
            index = int(input("Введите номер расхода: "))
            delete_expence(my_expenses, index)
        case "5":
            break
        case _:
            print("Некорректный выбор\n")
