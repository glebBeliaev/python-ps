import json
from tasks.model import Task
from helpers.table import format_date
from helpers.args import parse_date


def save_tasks(path: str, tasks: list[Task]):
    data = {
        "tasks": [
            {
                "id": task["id"],
                "title": task["title"],
                "priority": task["priority"],
                "due": format_date(task["due"]) if task["due"] else None,
                "tags": task["tags"],
                "status": task["status"],
            }
            for task in tasks
        ]
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Задачи сохранены в {path}")


def load_tasks(path: str) -> tuple[list[Task], int]:
    raw = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError as e:
        print(f"[ERROR]: Поврежден JSON ({path}): {e}")
        return [], 1
    task: list(Task) = []
    max_id = 0
    for item in raw.get("tasks", []):
        try:
            task: Task = {
                "id": int(item["id"]),
                "title": item["title"],
                "priority": item["priority"],
                "due": parse_date(item["due"]) if item["due"] else None,
                "tags": list(item.get("tags") or []),
                "status": item["status"],
            }
            tasks.append(task)
            max_id = max(max_id, task["id"])
        except Exception as e:
            print(f"[ERROR]: Пропущена задача: {e}")
    return tasks, max_id + 1
