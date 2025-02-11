from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

# Modelo de la tabla usuarios
class UsuarioTable(Base):
    __tablename__ = "usuarios"
 
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    habitaciones = relationship("Habitacion", back_populates="usuario")
