# **Описание**: Создайте функцию reduce_list, которая принимает список чисел, начальное значение и функцию-редуктор, и возвращает единственное значение, полученное последовательным применением функции к элементам списка.
#
# **Входные данные**: Функция reduce_list принимает три аргумента: numbers (список целых чисел), initial (начальное значение), reducer_func (функция, принимающая два аргумента и возвращающая одно значение)
#
# **Выходные данные**: Единственное значение, полученное последовательным применением reducer_func к элементам списка, начиная с initial
#
# **Ограничения**: Список содержит от 2 до 6 целых чисел от -15 до 15, initial - целое число от -10 до 10
#
# **Примеры**:
# Input: reduce_list([1, 2, 3], 0, lambda acc, x: acc + x)
# Output: 6
#
# Входные данные: reduce_list([2, 3, 4], 1, lambda acc, x: acc * x)
# Output: 24


def reduce_list(numbers, initial, reducer_func):
    result = initial
    for num in numbers:
        result = reducer_func(result, num)
    return result


# Тестирование
if __name__ == "__main__":
    result1 = reduce_list([1, 2, 3], 0, lambda acc, x: acc + x)
    print(result1)

    result2 = reduce_list([2, 3, 4], 1, lambda acc, x: acc * x)
    print(result2)

    result3 = reduce_list([1, 2, 3, 4, 5], 0, lambda acc, x: acc + x)
    print(result3)
