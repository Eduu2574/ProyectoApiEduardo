from pydantic import BaseModel
from typing import Optional

# Esquema para CREAR un hotel
class HotelCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria: str
    piscina: Optional[bool] = False
    localidad: str

# Esquema para ACTUALIZAR hotel
class UpdateHotel(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    piscina: Optional[bool] = None
    localidad: Optional[str] = None

# Esquema para RESPUESTA de hotel (con ID)
class HotelResponse(BaseModel):
    idHotel: int  # Cambié de id a idHotel
    nombre: str
    descripcion: Optional[str]
    categoria: str
    piscina: Optional[bool]
    localidad: str

    class Config:
        orm_mode = True  # Esto permit