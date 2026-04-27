"""Модуль работы с заказами"""

from typing import TypedDict, Optional
from datetime import date, datetime


STATUSES = ["new", "in_progress", "done", "cancelled"]
orders = []


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[list[str]]
    created_at: str
    due: Optional[date]
    closed_at: Optional[date]


def create_order(
    id_: int,
    title: str,
    amount: float,
    email: str,
    status: str,
    tags: Optional[list[str]] = None,
    due: Optional[date] = None,
    closed_at: Optional[date] = None,
):
    if status not in STATUSES:
        raise ValueError(f"Status must be one of {STATUSES}")
    order: Order = {
        "id": id_,
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "due": due,
        "closed_at": closed_at,
    }
    return order


def list_orders(orders: list[Order]):
    for order in orders:
        print(order)


def edit_order(
    id_: int,
    orders: list[Order],
    title: str,
    amount: float,
    email: str,
    status: str,
    tags: Optional[list[str]] = None,
    due: Optional[date] = None,
    closed_at: Optional[date] = None,
):
    for order in orders:
        if order["id"] == id_:
            order["title"] = title
            order["amount"] = amount
            order["email"] = email
            order["status"] = status
            order["tags"] = tags
            order["due"] = due
            order["closed_at"] = closed_at
            break
    else:
        raise ValueError(f"Order with id {id_} not found")

    return orders


def remove_order(id_: int, orders: list[Order]):
    for order in orders:
        if order["id"] == id_:
            orders.remove(order)
            break
    else:
        raise ValueError(f"Order with id {id_} not found")

    return orders
