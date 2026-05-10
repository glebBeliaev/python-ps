"""Модуль хранилища данных."""

import json
from orders import Order
from utils.helpers import parse_date


def load(path: str) -> tuple[list[Order], int]:
    """Загрузка данных из файла."""
    raw = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError as e:
        print(f"[ERROR]: Поврежден JSON ({path}): {e}")
        return [], 1

    orders: list[Order] = []
    max_id = 0
    for item in raw.get("orders", []):
        try:
            order: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": item["amount"],
                "email": item["email"],
                "status": item["status"],
                "tags": list(item.get("tags") or []),
                "created_at": item["created_at"],
                "due": parse_date(item["due"]) if item["due"] else None,
                "closed_at": item["closed_at"],
            }
            orders.append(order)
            max_id = max(max_id, order["id"])
        except Exception as e:
            print(f"[ERROR]: Пропущен заказ: {e}")
    return orders, max_id


def save(path: str, orders: list[Order]):
    data_orders = {
        "orders": [
            {
                "id": order["id"],
                "title": order["title"],
                "amount": order["amount"],
                "email": order["email"],
                "status": order["status"],
                "tags": order["tags"],
                "created_at": parse_date(order["created_at"]),
                "due": parse_date(order["due"]) if order["due"] else None,
                "closed_at": order["closed_at"],
            }
            for order in orders
        ]
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data_orders, f, ensure_ascii=False, indent=2)
