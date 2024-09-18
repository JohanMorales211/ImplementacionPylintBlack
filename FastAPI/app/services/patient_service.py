from models import PatientModel, DoctorModel
from peewee import DoesNotExist

class PatientService:
    """Service layer for Patient operations"""

    @staticmethod
    def create_patient(name: str, date_of_birth: str, doctor_id: int) -> PatientModel:
        """Create a new patient"""
        doctor = DoctorModel.get_by_id(doctor_id)
        patient = PatientModel.create(name=name, date_of_birth=date_of_birth, doctor_id=doctor)
        return patient

    @staticmethod
    def get_patient_by_id(patient_id: int) -> PatientModel:
        """Retrieve a patient by ID"""
        try:
            patient = PatientModel.get(PatientModel.id == patient_id)
            return patient
        except DoesNotExist:
            return None

    @staticmethod
    def update_patient(patient_id: int, name: str = None, date_of_birth: str = None, doctor_id: int = None) -> PatientModel:
        """Update an existing patient"""
        patient = PatientService.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if date_of_birth:
                patient.date_of_birth = date_of_birth
            if doctor_id:
                patient.doctor_id = DoctorModel.get_by_id(doctor_id)
            patient.save()
            return patient
        return None

    @staticmethod
    def delete_patient(patient_id: int) -> bool:
        """Delete a patient by ID"""
        patient = PatientService.get_patient_by_id(patient_id)
        if patient:
            patient.delete_instance()
            return True
        return False
