from models import DoctorModel
from peewee import DoesNotExist

class DoctorService:
    """Service layer for Doctor operations"""

    @staticmethod
    def create_doctor(name: str, specialty: str) -> DoctorModel:
        """Create a new doctor"""
        doctor = DoctorModel.create(name=name, specialty=specialty)
        return doctor

    @staticmethod
    def get_doctor_by_id(doctor_id: int) -> DoctorModel:
        """Retrieve a doctor by ID"""
        try:
            doctor = DoctorModel.get(DoctorModel.id == doctor_id)
            return doctor
        except DoesNotExist:
            return None

    @staticmethod
    def update_doctor(doctor_id: int, name: str = None, specialty: str = None) -> DoctorModel:
        """Update an existing doctor"""
        doctor = DoctorService.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
            doctor.save()
            return doctor
        return None

    @staticmethod
    def delete_doctor(doctor_id: int) -> bool:
        """Delete a doctor by ID"""
        doctor = DoctorService.get_doctor_by_id(doctor_id)
        if doctor:
            doctor.delete_instance()
            return True
        return False
