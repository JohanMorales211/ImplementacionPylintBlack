"""
This module contains the Product and Category models.
"""

from pydantic import BaseModel

class Product(BaseModel):
    """
    Product model representing a product with an id, name, description, price, and category_id.
    """
    id: int
    name: str
    description: str
    price: float
    category_id: int

class Category(BaseModel):
    """
    Category model representing a product category with an id and a name.
    """
    id: int
    name: str
