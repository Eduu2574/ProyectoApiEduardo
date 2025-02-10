from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL de la base de datos
SQLALCHEMY_DATABASE_URL = "postgresql://odoo:odoo@localhost:5342/hotelapiedu-database"

'''
postgresql: El tipo de base de datos.
odoo:odoo: Las credenciales de usuario (usuario: odoo, contraseña: odoo).
localhost:5342: Dirección del servidor de base de datos (localhost y puerto 5342).
fastapi-database: Nombre de la base de datos.
'''

#Crea el motor de conexión (engine) que interactuará con la base de datos utilizando la URL especificada.
engine = create_engine(SQLALCHEMY_DATABASE_URL)
#Configura un generador de sesiones
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
#Crea una clase base llamada Base, que se utiliza para definir los modelos de tablas de la base de datos. Los modelos heredan de esta clase.
Base = declarative_base()

def get_db():
    db = SessionLocal()  #Crear una nueva sesión
    try:
        yield db  #Devuelvo la sesión para su uso
    except Exception as e:
        print(e)
    finally:
        db.close()  #Cierro la sesión después de usarla