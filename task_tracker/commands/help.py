"""Модуль справки"""


def help_command():
    print(
        """Команды:
add <title> [priority=low|medium|high] [due=YYYY-MM-DD] [tags=a,b,c]- добавить задачу
list - вывести список задач
done <id> - завершить задачу
remove <id> - удалить задачу
edit <id> <title> [priority=low|medium|high] [YYYY-MM-DD] [tags=a,b,c] - изменить задачу
exit - завершить программу
"""
    )
