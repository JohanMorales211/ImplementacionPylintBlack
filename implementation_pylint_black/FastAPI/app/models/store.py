"""
This module contains the Store and Inventory models.
"""

from pydantic import BaseModel

class Store(BaseModel):
    """
    Store model representing a store with an id, name, and address.
    """
    id: int
    name: str
    address: str

class Inventory(BaseModel):
    """
    Inventory model representing a store's inventory with an id, store_id, product_id, and quantity.
    """
    id: int
    store_id: int
    product_id: int
    quantity: int
