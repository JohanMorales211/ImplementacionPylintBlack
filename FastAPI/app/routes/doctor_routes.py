from fastapi import APIRouter, HTTPException
from services.doctor_service import DoctorService

router = APIRouter()

@router.post("/doctors/")
def create_doctor(name: str, specialty: str):
    doctor = DoctorService.create_doctor(name, specialty)
    return doctor

@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    doctor = DoctorService.get_doctor_by_id(doctor_id)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.put("/doctors/{doctor_id}")
def update_doctor(doctor_id: int, name: str = None, specialty: str = None):
    doctor = DoctorService.update_doctor(doctor_id, name, specialty)
    if doctor:
        return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")

@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):
    if DoctorService.delete_doctor(doctor_id):
        return {"message": "Doctor deleted successfully"}
    raise HTTPException(status_code=404, detail="Doctor not found")
