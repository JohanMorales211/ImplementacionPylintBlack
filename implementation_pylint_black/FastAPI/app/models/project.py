"""
This module contains the Project, EmployeeProject and Task models.
"""

from pydantic import BaseModel

class Project(BaseModel):
    """
    Project model representing a project with an id, name, description, start date, and end date.
    """
    id: int
    name: str
    description: str
    start_date: str
    end_date: str

class EmployeeProject(BaseModel):
    """
    Employee model representing an employee with an id, name, email, phone, and position.
    """
    id: int
    name: str
    email: str
    phone: str
    booth: str

class Task(BaseModel):
    """
    Task model representing a task.
    """
    id: int
    project_id: int
    employee_id: int
    title: str
    description: str
    deadline_date: str
    state: str
