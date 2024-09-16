"""
This module contains the Employee and Department models.
"""

from pydantic import BaseModel

class Employee(BaseModel):
    """
    Employee model representing an employee with an id, name, email, phone, and department_id.
    """
    id: int
    name: str
    email: str
    phone: str
    department_id: int

class Department(BaseModel):
    """
    Department model representing a department with an id, name, and location.
    """
    id: int
    name: str
    location: str
