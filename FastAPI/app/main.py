"""
Main module for the FastAPI application.

This module creates and configures the FastAPI application instance,
registers routers for different routes, and includes the API documentation.
"""

from fastapi import FastAPI
from routes import doctor_router, patient_router

app = FastAPI()

# Register the routers with prefixes
app.include_router(doctor_router, prefix="/api/doctors")
app.include_router(patient_router, prefix="/api/patients")
