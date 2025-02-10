from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL de la base de datos
SQLALCHEMY_DATABASE_URL = "postgresql://odoo:odoo@localhost:5342/hotelapiedu-database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
#Configura un generador de sesiones
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
#Crea una clase base llamada Base, para definir los modelos de tablas de la base de datos.

def get_db():
    db = SessionLocal()  #Crear una nueva sesión
    try:
        yield db  #Devuelvo la sesión para su uso
    except Exception as e:
        print(e)
    finally:
        db.close()  #Cierro la sesión después de usarla