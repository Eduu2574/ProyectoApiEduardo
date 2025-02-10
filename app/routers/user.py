from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UpdateUser, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# OBTENER TODOS LOS USUARIOS
@router.get("/", response_model=List[UserResponse])
def obtener_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()

# CREAR UN NUEVO USUARIO (sin usar user_crud.py)
@router.post("/", summary="Crear un nuevo usuario", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# OBTENER UN USUARIO POR ID
@router.get("/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# ACTUALIZAR UN USUARIO
@router.put("/{user_id}", response_model=UserResponse, summary="Actualizar un usuario")
def update_user_info(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user.username:
        db_user.username = user.username
    if user.password:
        db_user.password = user.password
    if user.email:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user

# ELIMINAR UN USUARIO
@router.delete("/{user_id}", summary="Eliminar un usuario", response_model=UserResponse)
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return user