"""
This module contains the Ticket and Event models.
"""

from pydantic import BaseModel

class Ticket(BaseModel):
    """
    Ticket model representing a ticket with an id, event_id, user_id, and purchase date.
    """
    id: int
    event_id: int
    user_id: int
    purchase_date: str

class Event(BaseModel):
    """
    Event model representing an event with an id, name, date, and location.
    """
    id: int
    name: str
    date: str
    location: str
