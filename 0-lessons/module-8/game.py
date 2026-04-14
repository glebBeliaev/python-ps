import random

a = ["камень", "ножницы", "бумага"]
rounds = int(input("Введите количество раундов: "))
player_win = 0
computer_win = 0

for i in range(rounds):
    print(f"\nРаунд {i + 1}:")
    player_choice = ""
    while player_choice not in a:
        player_choice = input(
            "Некорректный выбор. Введите свой выбор (камень, ножницы, бумага): "
        ).lower()
    computer_choice = random.choice(a)
    print(f"Компьютер выбрал: {computer_choice}\n")

    if player_choice == computer_choice:
        print("Ничья!\n")
    elif (
        (player_choice == "камень" and computer_choice == "ножницы")
        or (player_choice == "ножницы" and computer_choice == "бумага")
        or (player_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы победили!\n")
        player_win += 1
    else:
        print("Вы проиграли!\n")
        computer_win += 1

print(f"Счет {player_win}:{computer_win}")
if player_win > computer_win:
    print("Игра завершена: Вы победили!")
elif player_win < computer_win:
    print("Игра завершена: Вы проиграли!")
else:
    print("Игра завершена: Ничья!")
