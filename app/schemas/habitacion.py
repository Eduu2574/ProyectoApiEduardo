from pydantic import BaseModel
from typing import Optional

# Esquema para CREAR una habitación
class HabitacionCreate(BaseModel):
    tamaio: str
    personas: Optional[int] = None
    precio: float
    desayuno: Optional[bool] = False
    ocupada: Optional[bool] = False
    idHotel: int  # Relación con el hotel

# Esquema para ACTUALIZAR habitación
class UpdateHabitacion(BaseModel):
    tamaio: Optional[str] = None
    personas: Optional[int] = None
    precio: Optional[float] = None
    desayuno: Optional[bool] = None
    ocupada: Optional[bool] = None


# Esquema para RESPUESTA de habitación (con ID)
class HabitacionResponse(BaseModel):
    idHabitacion: int  # Cambié de id a idHabitacion
    tamaio: str
    personas: Optional[int]
    precio: float
    desayuno: Optional[bool]
    ocupada: Optional[bool]
    idHotel: int  # Relación con el hotel

    class Config:
        orm_mode = True  # Permite que FastAPI convierta automáticamente el modelo SQLAlchemy a la respuesta Pydantic
