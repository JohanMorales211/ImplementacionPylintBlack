"""
This module contains the Reservation and Client models.
"""

from pydantic import BaseModel

class Reservation(BaseModel):
    """
    Reservation model representing a reservation with an id, client_id, date, and time.
    """
    id: int
    client_id: int
    date: str
    hour: str

class Client(BaseModel):
    """
    Client model representing a client with an id, name, phone, and email.
    """
    id: int
    name: str
    phone: str
    email: str
