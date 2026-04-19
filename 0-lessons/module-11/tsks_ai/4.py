# **Описание**:
# Создайте функцию filter_and_transform, которая принимает список чисел,
# функцию-фильтр и функцию-трансформатор, и возвращает новый список с трансформированными элементами, прошедшими фильтрацию.
#
# **Входные данные**: Функция filter_and_transform принимает три аргумента: numbers (список целых чисел), filter_func (функция, возвращающая True/False), transform_func (функция для преобразования числа)
#
# **Выходные данные**: Новый список, содержащий результаты применения transform_func к элементам, для которых filter_func вернула True
#
# **Ограничения**: Список содержит от 3 до 8 целых чисел от -20 до 20
#
# **Примеры**:
# Input: filter_and_transform([1, 2, 3, 4, 5], lambda x: x % 2 == 0, lambda x: x * 10)
# Output: [20, 40]
#
# Входные данные: filter_and_transform([-3, -1, 0, 2, 4], lambda x: x > 0, lambda x: x + 100)
# Output: [102, 104]


def filter_and_transform(numbers, filter_func, transform_func):
    return [transform_func(x) for x in numbers if filter_func(x)]


# Тестовые данные
test_data1 = [1, 2, 3, 4, 5]
test_data2 = [-3, -1, 0, 2, 4]

# Ваши тесты здесь

result1 = filter_and_transform(test_data1, lambda x: x % 2 == 0, lambda x: x * 10)
print(result1)

result2 = filter_and_transform(test_data2, lambda x: x > 0, lambda x: x + 100)
print(result2)
