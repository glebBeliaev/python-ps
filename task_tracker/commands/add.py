"""Модуль для добавления команды"""

from tasks.model import Task, make_task
from helpers.args import parse_add
from helpers.table import stringify_table


def add_command(tasks: list[Task], args: list[str], next_id: int) -> int:
    try:
        title, priority, due, tags = parse_add(args)
        task = make_task(1, title, priority, due, tags)
        tasks.append(task)
        print("Задача добавлена")
        print(stringify_table(tasks))
        return next_id + 1
    except ValueError as e:
        print(f"[ERROR]: {e}")
        return next_id
