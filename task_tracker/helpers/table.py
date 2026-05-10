"""Модуль для получения таблиц"""

from datetime import date

from tasks.model import Task


def format_date(d: date) -> str:
    return d.strftime("%Y-%m-%d")


def stringify_table(tasks: list[Task]) -> str:
    headers = ["id", "title", "status", "priority", "due", "tags"]
    rows: list[list[str]] = []

    for task in tasks:
        tags = ", ".join(sorted(task["tags"])) if task["tags"] else "-"

        rows.append(
            [
                str(task["id"]),
                task["title"],
                task["status"],
                task["priority"],
                format_date(task["due"]) if task["due"] else "-",
                tags,
            ]
        )

    col_widths = [len(header) for header in headers]

    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(col))

    def fmt_row(row: list[str]) -> str:
        return " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(row))

    out = [
        fmt_row(headers),
        "-+-".join("-" * width for width in col_widths),
    ]

    for row in rows:
        out.append(fmt_row(row))

    return "\n".join(out)
