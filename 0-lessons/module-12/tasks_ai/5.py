# **Описание**: Создайте функцию для проверки корректности email адреса с использованием кастомного исключения
#
# **Входные данные**: Строка с email адресом
#
# **Выходные данные**: Сообщение о результате проверки или сообщение об ошибке
#
# **Ограничения**:
# - Email должен содержать символ '@' и точку '.'
# - При некорректном email должно выбрасываться кастомное исключение InvalidEmailError
# - Функция должна обрабатывать исключения и возвращать соответствующие сообщения
# - При корректном email возвращайте "Email корректный: [email]"
# - При ошибке возвращайте "Ошибка: некорректный email адрес"
#
# **Примеры**:
# Входные данные: "user@example.com"
# Output: "Email корректный: user@example.com"
#
# Входные данные: "test@domain.org"
# Output: "Email корректный: test@domain.org"
#
# Входные данные: "invalid-email"
# Output: "Ошибка: некорректный email адрес"


# Ваш код здесь
class InvalidEmailError(Exception):
    pass


def validate_email(email: str):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Некорректный email адрес")

    return f"Email корректный: {email}"


def check_email_safely(email: str):
    try:
        return validate_email(email)
    except InvalidEmailError:
        return "Ошибка: некорректный email адрес"


# Примеры
print(check_email_safely("user@example.com"))
print(check_email_safely("test@domain.org"))
print(check_email_safely("invalid-email"))
