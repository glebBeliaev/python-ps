# **Описание**: Создайте функцию apply, которая принимает функцию и значение,
# и возвращает результат применения этой функции к значению.
#
# **Входные данные**: Функция apply принимает два аргумента: func (функция) и value (число)
#
# **Выходные данные**: Результат применения функции func к значению value
#
# **Ограничения**: value - целое число от -30 до 30
#
# **Примеры**:
# Input: apply(lambda x: x + 5, 10)
# Output: 15
#
# Входные данные: apply(lambda x: x * x, 4)
# Output: 16


def apply(func, value):
    return func(value)


# Тестирование
if __name__ == "__main__":
    result1 = apply(lambda x: x + 5, 10)
    print(result1)

    result2 = apply(lambda x: x * x, 4)
    print(result2)
