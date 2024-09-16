"""
This module contains the Doctor and Patient models.
"""

from pydantic import BaseModel

class Doctor(BaseModel):
    """
    Doctor model representing a doctor with an id, name, and specialty.
    """
    id: int
    name: str
    specialty: str

class Patient(BaseModel):
    """
    Patient model representing a patient with an id, name, birth date, and doctor_id.
    """
    id: int
    name: str
    date_born: str
    doctor_id: int
