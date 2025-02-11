from datetime import datetime
from pydantic import BaseModel, EmailStr

# Clase Usuario para crear y responder con la información del usuario
class Usuario(BaseModel):
    username: str
    correo: EmailStr  # Pydantic valida que sea un correo válido
    password: str
    fecha_registro: datetime = datetime.now()  # Fecha actual por defecto

# Clase para modificar un usuario
class UpdateUsuario(BaseModel):
    username: str = None
    correo: EmailStr = None
    password: str = None
