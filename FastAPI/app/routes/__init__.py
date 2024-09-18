from .doctor_routes import router as doctor_router
from .patient_routes import router as patient_router

# Definir qué routers estarán disponibles para la importación pública
__all__ = [
    "doctor_router",
    "patient_router",
]
