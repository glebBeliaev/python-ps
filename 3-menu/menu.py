category = input("Введите категорию (напиток, суп, десерт): ").lower()

order = ""

if category == "напиток":
    order = input("Введите напиток (чай, кофк, сок): ").lower()
elif category == "суп":
    order = input("Введите суп (борщ, щи, суп-пюре): ").lower()
elif category == "десерт":
    order = input("Введите десерт (торт, мороженое, фрукты): ").lower()
else:
    print("Категория не найдена")

match order:
    case "чай":
        print("Стоимость: 100р")
    case "кофе":
        print("Стоимость: 150р")
    case "сок":
        print("Стоимость: 50р")
    case "борщ":
        print("Стоимость: 200р")
    case "щи":
        print("Стоимость: 250р")
    case "суп-пюре":
        print("Стоимость: 300р")
    case "торт":
        print("Стоимость: 400р")
    case "мороженое":
        print("Стоимость: 500р")
    case "фрукты":
        print("Стоимость: 600р")
    case _:
        print("Товар не найден")
