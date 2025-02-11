from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# Modelo de la tabla Hotel
class Hotel(Base):
    __tablename__ = "hoteles"

    idHotel = Column(Integer, primary_key=True, autoincrement=True)  # Aquí 'idHotel' es la clave primaria
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    categoria = Column(String(50), nullable=False)
    piscina = Column(Boolean, default=False)
    localidad = Column(String(100), nullable=False)

    habitaciones = relationship("Habitacion", back_populates="hotel")
