import random

secret = random.randint(1, 10)
guess = 0

print("Угадайте число от 1 до 10")

while guess != secret:
    guess = int(input("Введите число: "))
    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")

print("Вы угадали!")
