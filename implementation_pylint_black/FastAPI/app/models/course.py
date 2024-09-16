"""
This module contains the Course and Instructor models.
"""

from pydantic import BaseModel

class Course(BaseModel):
    """
    Course model representing a course with an id, name, description, and instructor_id.
    """
    id: int
    name: str
    description: str
    instructor_id: int

class Instructor(BaseModel):
    """
    Instructor model representing an instructor with an id, name, and specialty.
    """
    id: int
    name: str
    specialty: str
