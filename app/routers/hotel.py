from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.hotel import Hotel
from app.schemas.hotel import HotelResponse, HotelCreate, UpdateHotel

router = APIRouter(
    prefix="/hoteles",
    tags=["Hoteles"]
)

# OBTENER TODOS LOS HOTELES
@router.get("/", response_model=List[HotelResponse])
def obtener_hoteles(db: Session = Depends(get_db)):
    return db.query(Hotel).all()

# CREAR UN NUEVO HOTEL
@router.post("/", response_model=HotelResponse, summary="Crear un nuevo hotel")
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    nuevo_hotel = Hotel(**hotel.dict())
    db.add(nuevo_hotel)
    db.commit()
    db.refresh(nuevo_hotel)
    return nuevo_hotel

# OBTENER UN HOTEL POR ID
@router.get("/{hotel_id}", response_model=HotelResponse, summary="Obtener un hotel por ID")
def get_hotel_by_id(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.idHotel == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")
    return hotel

# ACTUALIZAR UN HOTEL
@router.put("/{hotel_id}", response_model=HotelResponse, summary="Actualizar un hotel")
def update_hotel(hotel_id: int, hotel: UpdateHotel, db: Session = Depends(get_db)):
    db_hotel = db.query(Hotel).filter(Hotel.idHotel == hotel_id).first()
    if not db_hotel:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")

    for key, value in hotel.dict(exclude_unset=True).items():
        setattr(db_hotel, key, value)
    
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

# ELIMINAR UN HOTEL
@router.delete("/{hotel_id}", response_model=HotelResponse, summary="Eliminar un hotel")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.idHotel == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel no encontrado")
    
    db.delete(hotel)
    db.commit()
    return hotel
