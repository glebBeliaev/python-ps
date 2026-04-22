from typing import TypedDict

PRIORITIES = ["low", "med", "high"]


class Task(TypedDict):
    id: int
    title: str
    priority: str
    tags: list[str]
    status: str


def make_task(
    id_: int,
    title: str,
    priority: str = "med",
    tags: list[str] = [],
    status: str = "new",
):
    if priority not in PRIORITIES:
        raise ValueError(f"Priority must be one of {PRIORITIES}")
    task: Task = {
        "id": id_,
        "title": title,
        "priority": priority,
        "tags": tags,
        "status": status,
    }
    return task
