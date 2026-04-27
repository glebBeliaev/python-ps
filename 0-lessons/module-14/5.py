# **Описание**: Создайте программу для парсинга строки в объект datetime и обработки некорректного формата
# **Входные данные**: Строка с датой и временем в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС'
# **Выходные данные**: Объект datetime при корректном формате, или None при некорректном формате
# **Ограничения**: Используйте strptime для парсинга и обработайте ValueError при некорректном формате
# **Примеры**:
# Входные данные: '2025-03-15 14:30:45'
# Output: datetime(2025, 3, 15, 14, 30, 45)
# Входные данные: '2025-13-40 25:70:80'
# Output: None

from datetime import datetime

# Тестовые данные
date_string1 = "2025-03-15 14:30:45"
date_string2 = "2025-13-40 25:70:80"

# Ваш код здесь

try:
    parsed_date = datetime.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
    print(parsed_date)
except ValueError:
    print(None)

try:
    parsed_date = datetime.strptime(date_string2, "%Y-%m-%d %H:%M:%S")
    print(parsed_date)
except ValueError:
    print(None)
