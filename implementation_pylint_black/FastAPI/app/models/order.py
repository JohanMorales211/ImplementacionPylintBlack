"""
This module contains the Order and OrderProduct models.
"""

from pydantic import BaseModel

class Order(BaseModel):
    """
    Order model representing an order with an id, user_id, date, and total.
    """
    id: int
    user_id: int
    date: str
    total: float

class OrderProduct(BaseModel):
    """
    OrderProduct model representing a product in an order.
    """
    id: int
    order_id: int
    product_id: int
    quantity: int
