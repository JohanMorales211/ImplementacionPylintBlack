"""
Module that defines the routes for managing patients.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting patients through a REST API.

Available routes:

- POST /patients/: Creates a new patient.
- GET /patients/{patient_id}: Retrieves patient information by ID.
- PUT /patients/{patient_id}: Updates patient information.
- DELETE /patients/{patient_id}: Deletes a patient.

Each route uses the `PatientService` to interact with the
business logic related to patients.
"""

from fastapi import APIRouter, HTTPException
from services.patient_service import PatientService

router = APIRouter()


@router.post("/patients/")
def create_patient(name: str, date_of_birth: str, doctor_id: int):
    """Creates a new patient."""
    patient = PatientService.create_patient(name, date_of_birth, doctor_id)
    return patient


@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    """Retrieves patient information by ID."""
    patient = PatientService.get_patient_by_id(patient_id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@router.put("/patients/{patient_id}")
def update_patient(
    patient_id: int, name: str = None, date_of_birth: str = None, doctor_id: int = None
):
    """Updates patient information."""
    patient = PatientService.update_patient(
        patient_id, name, date_of_birth, doctor_id
    )
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    """Deletes a patient."""
    if PatientService.delete_patient(patient_id):
        return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")
