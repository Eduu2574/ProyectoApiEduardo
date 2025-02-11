from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import UsuarioTable
from app.schemas.user import UpdateUsuario, Usuario
from sqlalchemy.exc import IntegrityError

router = APIRouter(
    prefix="/usuario",
    tags=["Usuarios"]
)

# OBTENER TODOS LOS USUARIOS
@router.get("/obtener_usuarios")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioTable).all()
    return usuarios

# OBTENER USUARIO POR ID
@router.get("/obtener_usuario_por_id/{user_id}")
def obtener_usuario_por_id(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioTable).filter(UsuarioTable.idUsuario == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# CREAR UN NUEVO USUARIO
@router.post("/crear_usuario", response_model=Usuario)
def crear_usuario(user: Usuario, db: Session = Depends(get_db)):
    try:
        # Verificación si el correo ya existe
        db_user_by_email = db.query(UsuarioTable).filter(UsuarioTable.correo == user.correo).first()
        if db_user_by_email:
            raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso.")
        
        nuevo_usuario = UsuarioTable(
            username=user.username,
            correo=user.correo,
            password=user.password
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al crear el usuario: " + str(e.orig))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado al crear el usuario: {str(e)}")

# ELIMINAR UN USUARIO POR SU ID
@router.delete("/eliminar_usuario/{user_id}")
def eliminar_usuario_por_id(user_id: int, db: Session = Depends(get_db)):
    deleteUser = db.query(UsuarioTable).filter(UsuarioTable.idUsuario == user_id).first()
    if not deleteUser:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(deleteUser)
    db.commit()
    return {"Respuesta": "Usuario eliminado correctamente"}

# MODIFICAR USUARIOS
@router.patch("/modificar_usuario/{user_id}", response_model=Usuario)
def actualizar_usuario_por_id(user_id: int, updateUser: UpdateUsuario, db: Session = Depends(get_db)):
    actualizarUser = db.query(UsuarioTable).filter(UsuarioTable.idUsuario == user_id).first()
    if not actualizarUser:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if updateUser.username:
        actualizarUser.username = updateUser.username
    if updateUser.correo:
        actualizarUser.correo = updateUser.correo
    if updateUser.password:
        actualizarUser.password = updateUser.password

    db.commit()
    db.refresh(actualizarUser)
    return actualizarUser
