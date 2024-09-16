"""
This module contains the Author and Book models.
"""

from pydantic import BaseModel

class Author(BaseModel):
    """
    Author model representing an author with an id, name, and nationality.
    """
    id: int
    name: str
    nationality: str

class Book(BaseModel):
    """
    Book model representing a book with an id, title, author_id, and publication date.
    """
    id: int
    title: str
    author_id: int
    publication_date: str
