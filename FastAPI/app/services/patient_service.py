# app/patient_services.py

from typing import Optional
from peewee import DoesNotExist
from database import PatientModel, DoctorModel
from models.patient import Patient
from models.doctor import Doctor

class PatientService:
    """Service layer for Patient operations"""

    @staticmethod
    def create_patient(name: str, date_of_birth: str, doctor_id: int) -> Patient:
        """
        Create a new patient.
        
        Args:
            name (str): The name of the patient.
            date_of_birth (str): The birthdate of the patient.
            doctor_id (int): The ID of the assigned doctor.
        
        Returns:
            Patient: The created patient instance.
        
        Raises:
            ValueError: If the doctor with the given ID does not exist.
        """
        try:
            doctor_instance = DoctorModel.get_by_id(doctor_id)  # Obtener el doctor por ID
            patient_instance = PatientModel.create(name=name, date_of_birth=date_of_birth, doctor_id=doctor_instance)
            return Patient(id=patient_instance.id, name=patient_instance.name, date_born=patient_instance.date_of_birth, doctor_id=patient_instance.doctor_id.id)
        except DoesNotExist:
            raise ValueError(f"Doctor with id {doctor_id} not found")

    @staticmethod
    def get_patient_by_id(patient_id: int) -> Optional[Patient]:
        """
        Retrieve a patient by ID.
        
        Args:
            patient_id (int): The ID of the patient to retrieve.
        
        Returns:
            Optional[Patient]: The patient instance if found, else None.
        """
        try:
            patient_instance = PatientModel.get_by_id(patient_id)
            return Patient(id=patient_instance.id, name=patient_instance.name, date_born=patient_instance.date_of_birth, doctor_id=patient_instance.doctor_id.id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_patient(patient_id: int, name: Optional[str] = None, date_of_birth: Optional[str] = None, doctor_id: Optional[int] = None) -> Optional[Patient]:
        """
        Update an existing patient by ID.
        
        Args:
            patient_id (int): The ID of the patient to update.
            name (Optional[str]): The new name of the patient.
            date_of_birth (Optional[str]): The new birthdate of the patient.
            doctor_id (Optional[int]): The new doctor's ID.
        
        Returns:
            Optional[Patient]: The updated patient instance if successful, else None.
        
        Raises:
            ValueError: If the doctor with the given ID does not exist.
        """
        patient_instance = PatientService.get_patient_by_id(patient_id)
        if patient_instance:
            if name:
                patient_instance.name = name
            if date_of_birth:
                patient_instance.date_of_birth = date_of_birth
            if doctor_id:
                try:
                    doctor_instance = DoctorModel.get_by_id(doctor_id)
                    patient_instance.doctor_id = doctor_instance
                except DoesNotExist:
                    raise ValueError(f"Doctor with id {doctor_id} not found")
            patient_instance.save()
            return Patient(id=patient_instance.id, name=patient_instance.name, date_born=patient_instance.date_of_birth, doctor_id=patient_instance.doctor_id.id)
        return None

    @staticmethod
    def delete_patient(patient_id: int) -> bool:
        """
        Delete a patient by ID.
        
        Args:
            patient_id (int): The ID of the patient to delete.
        
        Returns:
            bool: True if the patient was deleted, else False.
        """
        patient_instance = PatientService.get_patient_by_id(patient_id)
        if patient_instance:
            patient_instance.delete_instance()
            return True
        return False

