# **Описание**: Создайте функцию для обработки списка словарей с использованием assert для проверки структуры данных
#
# **Входные данные**: Список словарей, где каждый словарь должен содержать ключи 'name' и 'score'
#
# **Выходные данные**: Список имен пользователей с высокими баллами (score >= 80)
#
# **Ограничения**:
# - Используйте assert для проверки наличия ключей 'name' и 'score' в каждом словаре
# - Используйте блок try для выполнения проверки assert
# - Используйте блок except для перехвата AssertionError
# - При ошибке assert выведите "Ошибка структуры данных: словарь не содержит необходимые ключи"
# - Функция должна возвращать список имен с баллами >= 80
# - Обрабатывайте каждый словарь в цикле
#
# **Примеры**:
# Входные данные: [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 75}, {'name': 'Charlie', 'score': 90}]
# Output: ['Alice', 'Charlie']
#
# Входные данные: [{'name': 'John', 'score': 95}, {'name': 'Jane'}, {'name': 'Mike', 'score': 88}]
# Output: Ошибка структуры данных: словарь не содержит необходимые ключи
# Output: ['John', 'Mike']


def process_user_scores(users):
    high_scores = []

    for user in users:
        try:
            assert "name" in user and "score" in user

            if user["score"] >= 80:
                high_scores.append(user["name"])

        except AssertionError:
            print("Ошибка структуры данных: словарь не содержит необходимые ключи")

    return high_scores


# Тестовые данные
test_data1 = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 90},
]

test_data2 = [
    {"name": "John", "score": 95},
    {"name": "Jane"},
    {"name": "Mike", "score": 88},
]

# Вызовы функции
result1 = process_user_scores(test_data1)
print(result1)

result2 = process_user_scores(test_data2)
print(result2)

# Ожидаемые результаты
expected_result1 = ["Alice", "Charlie"]
expected_result2 = ["John", "Mike"]
