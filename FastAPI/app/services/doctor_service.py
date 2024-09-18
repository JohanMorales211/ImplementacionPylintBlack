class DoctorService:
    """Service layer for Doctor operations"""

    @staticmethod
    def create_doctor(name: str, specialty: str) -> Doctor:
        """
        Create a new doctor.
        
        Args:
            name (str): The name of the doctor.
            specialty (str): The doctor's specialty.
        
        Returns:
            Doctor: The created doctor instance.
        """
        doctor_instance = Doctor.create(name=name, specialty=specialty)
        return doctor_instance

    @staticmethod
    def get_doctor_by_id(doctor_id: int) -> Doctor:
        """
        Retrieve a doctor by ID.
        
        Args:
            doctor_id (int): The ID of the doctor to retrieve.
        
        Returns:
            Doctor or None: The doctor instance if found, else None.
        """
        try:
            doctor_instance = Doctor.get(Doctor.id == doctor_id)
            return doctor_instance
        except DoesNotExist:
            return None

    @staticmethod
    def update_doctor(doctor_id: int, name: str = None, specialty: str = None) -> Doctor:
        """
        Update an existing doctor by ID.
        
        Args:
            doctor_id (int): The ID of the doctor to update.
            name (str, optional): The new name of the doctor.
            specialty (str, optional): The new specialty of the doctor.
        
        Returns:
            Doctor or None: The updated doctor instance if successful, else None.
        """
        doctor_instance = DoctorService.get_doctor_by_id(doctor_id)
        if doctor_instance:
            if name:
                doctor_instance.name = name
            if specialty:
                doctor_instance.specialty = specialty
            doctor_instance.save()
            return doctor_instance
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
