# если слово СПАМ останавливаем проверку
# если сообщение больше 20 символов пропускаем
# вывести был ли спам
messages = [
    "Привет",
    "Купи дешевые курсы!!!",
    "Как дела?",
    "СПАМ реклама!!!",
    "Пойдем играть в футбол?",
]
spam = False
for message in messages:
    if "СПАМ" in message:
        spam = True
        break
    elif len(message) > 20:
        continue

if spam:
    print("Был найден спам")
