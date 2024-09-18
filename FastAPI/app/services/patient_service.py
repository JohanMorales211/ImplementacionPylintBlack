from models.patient import Patient  # Importamos el modelo Patient
from models.doctor import Doctor  # Importamos el modelo Doctor
from peewee import DoesNotExist

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
        """
        doctor_instance = Doctor.get_by_id(doctor_id)  # Obtener el doctor por ID
        patient_instance = Patient.create(name=name, date_of_birth=date_of_birth, doctor_id=doctor_instance)
        return patient_instance

    @staticmethod
    def get_patient_by_id(patient_id: int) -> Patient:
        """
        Retrieve a patient by ID.
        
        Args:
            patient_id (int): The ID of the patient to retrieve.
        
        Returns:
            Patient or None: The patient instance if found, else None.
        """
        try:
            patient_instance = Patient.get(Patient.id == patient_id)
            return patient_instance
        except DoesNotExist:
            return None

    @staticmethod
    def update_patient(patient_id: int, name: str = None, date_of_birth: str = None, doctor_id: int = None) -> Patient:
        """
        Update an existing patient by ID.
        
        Args:
            patient_id (int): The ID of the patient to update.
            name (str, optional): The new name of the patient.
            date_of_birth (str, optional): The new birthdate of the patient.
            doctor_id (int, optional): The new doctor's ID.
        
        Returns:
            Patient or None: The updated patient instance if successful, else None.
        """
        patient_instance = PatientService.get_patient_by_id(patient_id)
        if patient_instance:
            if name:
                patient_instance.name = name
            if date_of_birth:
                patient_instance.date_of_birth = date_of_birth
            if doctor_id:
                patient_instance.doctor_id = Doctor.get_by_id(doctor_id)
            patient_instance.save()
            return patient_instance
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
