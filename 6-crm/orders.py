"""Модуль работы с заказами"""

from typing import TypedDict

STATUSES = ["new", "in_progress", "done", "cancelled"]


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: list[str]
    tags: set[str]
    created_at: str
    due: str
    closed_at: str


def create_order():
    pass


def list_orders():
    pass


def edit_order():
    pass


def remove_order():
    pass
