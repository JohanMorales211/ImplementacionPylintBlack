"""
Main module for the FastAPI application.

This module creates and configures the FastAPI application instance,
registers routers for different routes, and includes the API documentation.
"""

from app.routes import doctor_router
from app.routes import patient_router
from fastapi import FastAPI


app = FastAPI()

# Register the routers with prefixes
app.include_router(doctor_router, prefix="/api/doctors")
app.include_router(patient_router, prefix="/api/patients")
