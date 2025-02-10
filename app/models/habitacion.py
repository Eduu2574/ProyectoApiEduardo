from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Modelo de la tabla Habitacion
class Habitacion(Base):
    __tablename__ = "habitaciones"

    idHabitacion = Column(Integer, primary_key=True, autoincrement=True)
    tamaio = Column(String(100), nullable=False)
    personas = Column(Integer, nullable=True)
    precio = Column(Float, nullable=False)
    desayuno = Column(Boolean, nullable=True)
    ocupada = Column(Boolean, default=False)

    # Una habitación pertenece a un solo hotel
    idHotel = Column(Integer, ForeignKey("hoteles.idHotel"), nullable=False)
    hotel = relationship("Hotel", back_populates="habitaciones")

    # Una habitación puede ser reservada por un solo usuario a la vez
    idUsuario = Column(Integer, ForeignKey("usuarios.idUsuario"), nullable=True)
    usuario = relationship("User", back_populates="habitaciones")