"""Модуль разбора аргументов"""

from datetime import date, datetime


def parse_add(args: list[str]):
    if not args:
        raise ValueError(
            "Неверный формат. Ожидается add <title> [priority=low|medium|high] [due=YYYY-MM-DD] [tags=a,b,c]- добавить задачу"
        )
    title = args[0]
    priority, due, tags = "med", None, None
    for arg in args[1:]:
        if arg.startswith("priority="):
            priority = arg.split("=")[1]
        elif arg.startswith("due="):
            due_str = arg.split("=")[1]
            try:
                due = parse_date(due_str)
            except ValueError as e:
                raise ValueError(
                    f"Неверный формат даты {due_str}. Ожидается YYYY-MM-DD"
                ) from e
        elif arg.startswith("tags="):
            tags_str = arg.split("=")[1]
            tags = tags_str.split(",")

        else:
            raise ValueError(
                "Неверный формат. Ожидается add <title> [priority=low|medium|high] [due=YYYY-MM-DD] [tags=a,b,c]- добавить задачу"
            )
    return title, priority, due, tags


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%Y-%m-%d").date()
