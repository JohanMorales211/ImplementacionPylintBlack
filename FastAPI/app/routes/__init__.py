"""
Initialization module for the routes package.

This module imports and makes available the routers for handling doctor and patient routes.

Modules:
    - doctor_routes: Contains the router for doctor-related routes.
    - patient_routes: Contains the router for patient-related routes.

Available Routers:
    - doctor_router: Router for doctor-related routes.
    - patient_router: Router for patient-related routes.
"""

from .doctor_routes import router as doctor_router
from .patient_routes import router as patient_router

# Definir qué routers estarán disponibles para la importación pública
__all__ = [
    "doctor_router",
    "patient_router",
]
