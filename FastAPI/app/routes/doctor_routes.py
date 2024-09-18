"""
Module that defines the routes for managing doctors.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting doctors through a REST API.

Available routes:

- POST /doctors/: Creates a new doctor.
- GET /doctors/{doctor_id}: Retrieves doctor information by ID.
- PUT /doctors/{doctor_id}: Updates doctor information.
- DELETE /doctors/{doctor_id}: Deletes a doctor.

Each route uses the `DoctorService` to interact with the
business logic related to doctors.
"""

from fastapi import APIRouter, HTTPException
from services.doctor_service import DoctorService

router = APIRouter()


@router.post("/doctors/")
def create_doctor(name: str, specialty: str):
    """Creates a new doctor."""
    doctor = DoctorService.create_doctor(name, specialty)
    return doctor


@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    """Retrieves doctor information by ID."""
    doctor = DoctorService.get_doctor_by_id(doctor_id)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.put("/doctors/{doctor_id}")
def update_doctor(doctor_id: int, name: str = None, specialty: str = None):
    """Updates doctor information."""
    doctor = DoctorService.update_doctor(doctor_id, name, specialty)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):
    """Deletes a doctor."""
    if DoctorService.delete_doctor(doctor_id):
        return {"message": "Doctor deleted successfully"}
    raise HTTPException(status_code=404, detail="Doctor not found")

