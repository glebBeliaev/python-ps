# **Описание**: Создайте функцию для обработки списка операций с использованием общего обработчика исключений
#
# **Входные данные**: Список кортежей, где каждый кортеж содержит операцию и два числа (операция, число1, число2)
#
# **Ограничения**:
# - Поддерживаемые операции: 'add', 'subtract', 'multiply', 'divide'
# - Используйте блок try для выполнения каждой операции
# - Используйте общий блок except Exception для перехвата любых исключений
# - При исключении выведите "Ошибка в операции [операция]: [текст исключения]"
# - При успешном выполнении добавьте результат в список результатов
# - Функция должна возвращать список всех успешно выполненных результатов
# - Обрабатывайте каждую операцию в цикле
#
# **Примеры**:
# Входные данные: [('add', 5, 3), ('divide', 10, 2), ('multiply', 4, 6)]
# Output: [8, 5.0, 24]
#
# Входные данные: [('add', 1, 2), ('divide', 8, 0), ('subtract', 10, 3)]
# Output: Ошибка в операции divide: division by zero
# Output: [3, 7]


def process_operations(operations):
    results = []

    for operation, num1, num2 in operations:
        try:
            if operation == "add":
                result = num1 + num2

            elif operation == "subtract":
                result = num1 - num2

            elif operation == "multiply":
                result = num1 * num2

            elif operation == "divide":
                result = num1 / num2

            else:
                raise ValueError("Неизвестная операция")

            results.append(result)

        except Exception as error:
            print(f"Ошибка в операции {operation}: {error}")

    return results


# Тестовые данные
operations1 = [
    ("add", 5, 3),
    ("divide", 10, 2),
    ("multiply", 4, 6),
]

operations2 = [
    ("add", 1, 2),
    ("divide", 8, 0),
    ("subtract", 10, 3),
]

print(process_operations(operations1))
print(process_operations(operations2))
