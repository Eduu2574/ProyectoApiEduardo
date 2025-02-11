from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.habitacion import Habitacion
from app.schemas.habitacion import HabitacionResponse, HabitacionCreate, UpdateHabitacion

router = APIRouter(
    prefix="/habitaciones",
    tags=["Habitaciones"]
)

# OBTENER TODAS LAS HABITACIONES
@router.get("/", response_model=List[HabitacionResponse])
def obtener_habitaciones(db: Session = Depends(get_db)):
    return db.query(Habitacion).all()

# CREAR UNA NUEVA HABITACIÓN
# CREAR UNA NUEVA HABITACIÓN
@router.post("/", response_model=HabitacionResponse, summary="Crear una nueva habitación")
def create_habitacion(habitacion: HabitacionCreate, db: Session = Depends(get_db)):
    nueva_habitacion = Habitacion(**habitacion.dict())  # Esto creará una nueva instancia de Habitacion
    db.add(nueva_habitacion)
    db.commit()
    db.refresh(nueva_habitacion)
    return nueva_habitacion  # Esto devuelve la nueva habitación
# OBTENER UNA HABITACIÓN POR ID
@router.get("/{habitacion_id}", response_model=HabitacionResponse, summary="Obtener una habitación por ID")
def get_habitacion_by_id(habitacion_id: int, db: Session = Depends(get_db)):
    habitacion = db.query(Habitacion).filter(Habitacion.idHabitacion == habitacion_id).first()
    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return habitacion

# ACTUALIZAR UNA HABITACIÓN
@router.put("/{habitacion_id}", response_model=HabitacionResponse, summary="Actualizar una habitación")
def update_habitacion(habitacion_id: int, habitacion: UpdateHabitacion, db: Session = Depends(get_db)):
    db_habitacion = db.query(Habitacion).filter(Habitacion.idHabitacion == habitacion_id).first()
    if not db_habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")

    for key, value in habitacion.dict(exclude_unset=True).items():
        setattr(db_habitacion, key, value)
    
    db.commit()
    db.refresh(db_habitacion)
    return db_habitacion

# ELIMINAR UNA HABITACIÓN
@router.delete("/{habitacion_id}", response_model=HabitacionResponse, summary="Eliminar una habitación")
def delete_habitacion(habitacion_id: int, db: Session = Depends(get_db)):
    habitacion = db.query(Habitacion).filter(Habitacion.idHabitacion == habitacion_id).first()
    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    
    db.delete(habitacion)
    db.commit()
    return habitacion

