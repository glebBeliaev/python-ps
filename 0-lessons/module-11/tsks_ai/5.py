# **Описание**:
# Создайте функцию make_counter, которая возвращает новую функцию-счётчик, увеличивающую внутреннее значение на 1 при каждом вызове.
#
# **Входные данные**: Функция make_counter не принимает аргументов. Возвращаемая функция также не принимает аргументов.
#
# **Выходные данные**: Возвращаемая функция должна возвращать текущее значение счётчика (начиная с 1)
#
# **Ограничения**: Счётчик должен начинаться с 0 и увеличиваться на 1 при каждом вызове
#
# **Примеры**:
# Input: counter = make_counter(); counter()
# Output: 1
#
# Входные данные: counter = make_counter(); counter(); counter()
# Output: 2


def make_counter():
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        return counter

    return increment


counter = make_counter()
print(counter())
print(counter())
print(counter())
