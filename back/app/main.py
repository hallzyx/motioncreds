from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.routers import user, test
# Define or carga tu lista de orígenes permitidos
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
    # Agrega aquí otros orígenes si los requieres
]

def create_tables():
    Base.metadata.create_all(bind=engine)
def start_app():
    create_tables()
    app =FastAPI(title="wasa")
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Lista de dominios permitidos
    allow_credentials=True,        # Permite envío de cookies/autenticación
    allow_methods=["*"],           # Métodos HTTP permitidos
    allow_headers=["*"]            # Encabezados permitidos
)
    app.include_router(user.router)
    app.include_router(test.router)
    return app

app=start_app()