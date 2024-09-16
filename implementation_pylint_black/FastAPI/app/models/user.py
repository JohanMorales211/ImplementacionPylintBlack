"""
This module contains the User and Profile models.
"""

from pydantic import BaseModel

class User(BaseModel):
    """
    User model representing a user with an id, name, email, and password.
    """
    id: int
    name: str
    email: str
    password: str

class Profile(BaseModel):
    """
    Profile model representing a user's profile with an id, user_id, profile picture, and biography.
    """
    id: int
    user_id: int
    profile_photo: str
    biography: str
