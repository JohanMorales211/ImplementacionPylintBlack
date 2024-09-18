from fastapi import FastAPI
from routes import doctor_router, patient_router

app = FastAPI()

# Registrar los routers de doctors y patients con prefijos y etiquetas
app.include_router(doctor_router, prefix="/api/doctors", tags=["Doctors"])
app.include_router(patient_router, prefix="/api/patients", tags=["Patients"])

