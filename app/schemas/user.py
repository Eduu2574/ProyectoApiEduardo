from pydantic import BaseModel, EmailStr
from typing import Optional

# Esquema para CREAR un usuario (sin ID porque la BD lo genera)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Esquema para ACTUALIZAR usuario (todos los campos opcionales)
class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Esquema para RESPUESTA de usuario (con ID)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
