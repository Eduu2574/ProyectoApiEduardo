from fastapi import FastAPI 
import uvicorn
from app.routers import jwt, user,hotel,habitacion
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

app.include_router(jwt.router)
app.include_router(user.router)
app.include_router(hotel.router)
app.include_router(habitacion.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)