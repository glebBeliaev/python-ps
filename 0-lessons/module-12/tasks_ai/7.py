# **Описание**: Создайте функцию для проверки корректности пароля с использованием нескольких блоков except
#
# **Входные данные**: Строка с паролем
#
# **Выходные данные**: Сообщение о результате проверки или сообщение об ошибке
#
# **Ограничения**:
# - Пароль должен быть длиной от 6 до 20 символов
# - При слишком коротком пароле (менее 6 символов) выбрасывайте ValueError с сообщением "Пароль слишком короткий"
# - При слишком длинном пароле (более 20 символов) выбрасывайте ValueError с сообщением "Пароль слишком длинный"
# - При пустом пароле (None или пустая строка) выбрасывайте TypeError с сообщением "Пароль не может быть пустым"
# - Используйте отдельные блоки except для ValueError и TypeError
# - При корректном пароле возвращайте "Пароль принят"
# - При ValueError выводите "Ошибка длины: [текст ошибки]"
# - При TypeError выводите "Ошибка типа: [текст ошибки]"
#
# **Примеры**:
# Входные данные: "password123"
# Output: "Пароль принят"
#
# Входные данные: "abc"
# Output: Ошибка длины: Пароль слишком короткий
#
# Входные данные: "verylongpasswordthatexceedslimit"
# Output: Ошибка длины: Пароль слишком длинный


def validate_password(password):
    if password is None or password == "":
        raise TypeError("Пароль не может быть пустым")

    if len(password) < 6:
        raise ValueError("Пароль слишком короткий")

    if len(password) > 20:
        raise ValueError("Пароль слишком длинный")

    return "Пароль принят"


def check_password_safely(password):
    try:
        return validate_password(password)

    except ValueError as error:
        return f"Ошибка длины: {error}"

    except TypeError as error:
        return f"Ошибка типа: {error}"


# Примеры
print(check_password_safely("password123"))
print(check_password_safely("abc"))
print(check_password_safely("verylongpasswordthatexceedslimit"))
print(check_password_safely(""))
print(check_password_safely(None))
