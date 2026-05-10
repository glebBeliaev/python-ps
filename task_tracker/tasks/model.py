from typing import TypedDict, Optional
from datetime import date

PRIORITIES = ["low", "med", "high"]


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: Optional[list[str]]
    status: str
    due: Optional[date]


def make_task(
    id_: int,
    title: str,
    priority: str = "med",
    due: Optional[date] = None,
    tags: Optional[list[str]] = None,
    status: str = "new",
):
    if priority not in PRIORITIES:
        raise ValueError(f"Priority must be one of {PRIORITIES}")
    task: Task = {
        "id": id_,
        "title": title,
        "priority": priority,
        "due": due,
        "tags": tags,
        "status": status,
    }
    return task
