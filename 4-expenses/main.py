while True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice = input("\nВыберите пункт меню (1-5): ")
    if choice == "5":
        break
    else:
        print("Некорректный выбор\n")

# s = input("Введите сумму: ").lower().strip()
# parts = s.split()


# if len(parts) == 2 and parts[0].isdigit() and parts[1] == "руб":
#     rub = int(parts[0])
#     kop = 0
# elif (
#     len(parts) == 4
#     and parts[0].isdigit()
#     and parts[1] == "руб"
#     and parts[2].isdigit()
#     and parts[3] == "коп"
# ):
#     rub = int(parts[0])
#     kop = int(parts[2])

# else:
#     print("Некорректный формат суммы")
#     exit()

# print(f"{rub}.{kop:02d} ₽")
