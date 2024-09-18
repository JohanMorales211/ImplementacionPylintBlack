from fastapi import APIRouter, HTTPException
from services.patient_service import PatientService

router = APIRouter()

@router.post("/patients/")
def create_patient(name: str, date_of_birth: str, doctor_id: int):
    patient = PatientService.create_patient(name, date_of_birth, doctor_id)
    return patient

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    patient = PatientService.get_patient_by_id(patient_id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.put("/patients/{patient_id}")
def update_patient(patient_id: int, name: str = None, date_of_birth: str = None, doctor_id: int = None):
    patient = PatientService.update_patient(patient_id, name, date_of_birth, doctor_id)
    if patient:
        return patient
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    if PatientService.delete_patient(patient_id):
        return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")
