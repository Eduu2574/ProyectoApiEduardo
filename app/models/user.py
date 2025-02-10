from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Modelo de la tabla Usuario
class User(Base):
    __tablename__ = "usuarios"

    idUsuario = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # Un usuario puede reservar varias habitaciones (relación uno a muchos)
    habitaciones = relationship("Habitacion", back_populates="usuario")