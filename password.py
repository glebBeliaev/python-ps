import string, random

passwords: dict[str, str] = {}


def get_password() -> str:
    password = input("Введите пароль (пустой для генерации): ")
    if password == "":
        password = generate_password()
    return password


def show_passwords():
    if len(passwords) == 0:
        print("Список паролей пуст\n")
        return
    print("Domain".ljust(20), "|", "Password")
    print("-" * 40)
    for domain, password in passwords.items():
        print(domain.ljust(20), "|", password)
    print("-" * 40)


def add_password():
    domain = input("Введите домен: ")
    if domain in passwords:
        print("Домен уже существует\n")
        return
    password = get_password()
    passwords[domain] = password
    print("Пароль добавлен\n")


def delete_password():
    domain = input("Введите домен: ")
    if domain not in passwords:
        print("Домен не существует\n")
        return
    del passwords[domain]
    print("Пароль удален\n")


def generate_password(length: int = 8, use_symbols: bool = True):
    if length < 6:
        return ""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits
    if use_symbols:
        chars += symbols
    return "".join([random.choice(chars) for _ in range(length)])


def update_password():
    domain = input("Введите домен: ")
    if domain not in passwords:
        print("Домен не существует\n")
        return
    password = get_password()
    passwords[domain] = password
    print("Пароль обновлен\n")


def show_menu():
    print("1. Показать пароли")
    print("2. Добавить пароль")
    print("3. Удалить пароль")
    print("4. Обновить пароль")
    print("5. Выход")

    choice = input("\nВыберите пункт меню (1-5): ")
    match choice:
        case "1":
            show_passwords()
        case "2":
            add_password()
        case "3":
            delete_password()
        case "4":
            update_password()
        case "5":
            print("Выход")
        case _:
            print("Некорректный выбор")


while True:
    show_menu()
