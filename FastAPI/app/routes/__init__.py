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

from app.routes import doctor_routes
from app.routes import patient_routes

# Definir qué routers estarán disponibles para la importación pública
doctor_router=doctor_routes.router
patient_router=patient_routes.router
