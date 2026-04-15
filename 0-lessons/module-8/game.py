import random


def select_variant() -> str:
    choice = None

    while choice not in choises:
        choice = input("Введите свой выбор (камень, ножницы, бумага): ").lower()
        if choice not in choises:
            print("Некорректный выбор.\n")
    return choice


def compute_game_result(player_choice: str, computer_choice: str) -> tuple[int, int]:
    if player_choice == computer_choice:
        print("Ничья!\n")
        return (0, 0)
    elif (
        (player_choice == "камень" and computer_choice == "ножницы")
        or (player_choice == "ножницы" and computer_choice == "бумага")
        or (player_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы победили!\n")
        return (1, 0)
    else:
        print("Вы проиграли!\n")
        return (0, 1)


def print_result(player_win: int, computer_win: int):
    print(f"Счет {player_win}:{computer_win}")
    if player_win > computer_win:
        print("Игра завершена: Вы победили!")
    elif player_win < computer_win:
        print("Игра завершена: Вы проиграли!")
    else:
        print("Игра завершена: Ничья!")


choises = ["камень", "ножницы", "бумага"]
rounds = int(input("Введите количество раундов: "))
player_win = 0
computer_win = 0

for i in range(rounds):
    print(f"\nРаунд {i + 1}:")
    player_choice = select_variant()
    computer_choice = random.choice(choises)
    print(f"Компьютер выбрал: {computer_choice}\n")
    [user_mode, computer_mode] = compute_game_result(player_choice, computer_choice)
    player_win += user_mode
    computer_win += computer_mode
print_result(player_win, computer_win)
