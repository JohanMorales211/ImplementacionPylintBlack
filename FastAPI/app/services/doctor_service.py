"""
Service layer for Doctor operations.

This module contains the business logic for managing doctors.
It interacts with the `DoctorModel` from the database and uses
the `Doctor` Pydantic model for data validation.
"""

from typing import Optional
from peewee import DoesNotExist  # pylint: disable=import-error
from app.database import DoctorModel  # pylint: disable=import-error
from app.models.doctor import Doctor  # pylint: disable=import-error


class DoctorService:
    """Service layer for Doctor operations."""

    @staticmethod
    def create_doctor(name: str, specialty: str) -> Doctor:
        """
        Create a new doctor.

        Args:
            name (str): The name of the doctor.
            specialty (str): The specialty of the doctor.

        Returns:
            Doctor: The created doctor instance.
        """
        doctor_instance = DoctorModel.create(name=name, specialty=specialty)
        return Doctor(
            id=doctor_instance.id,
            name=doctor_instance.name,
            specialty=doctor_instance.specialty,
        )

    @staticmethod
    def get_doctor_by_id(doctor_id: int) -> Optional[Doctor]:
        """
        Retrieve a doctor by ID.

        Args:
            doctor_id (int): The ID of the doctor to retrieve.

        Returns:
            Optional[Doctor]: The doctor instance if found, else None.
        """
        try:
            doctor_instance = DoctorModel.get_by_id(doctor_id)
            return Doctor(
                id=doctor_instance.id,
                name=doctor_instance.name,
                specialty=doctor_instance.specialty,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_doctor(
        doctor_id: int, name: Optional[str] = None, specialty: Optional[str] = None
    ) -> Optional[Doctor]:
        """
        Update an existing doctor by ID.

        Args:
            doctor_id (int): The ID of the doctor to update.
            name (Optional[str]): The new name of the doctor.
            specialty (Optional[str]): The new specialty of the doctor.

        Returns:
            Optional[Doctor]: The updated doctor instance if successful, else None.
        """
        doctor_instance = DoctorService.get_doctor_by_id(doctor_id)
        if doctor_instance:
            if name:
                doctor_instance.name = name
            if specialty:
                doctor_instance.specialty = specialty
            doctor_instance.save()
            return Doctor(
                id=doctor_instance.id,
                name=doctor_instance.name,
                specialty=doctor_instance.specialty,
            )
        return None

    @staticmethod
    def delete_doctor(doctor_id: int) -> bool:
        """
        Delete a doctor by ID.

        Args:
            doctor_id (int): The ID of the doctor to delete.

        Returns:
            bool: True if the doctor was deleted, else False.
        """
        doctor_instance = DoctorService.get_doctor_by_id(doctor_id)
        if doctor_instance:
            doctor_instance.delete_instance()
            return True
        return False
