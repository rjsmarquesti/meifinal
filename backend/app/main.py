from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Importações dos roteadores
from app.routers.auth import router as auth_router
# Tente importar os outros, se existirem
try:
    from app.routers.clientes import router as clientes_router
except ImportError:
    clientes_router = None

try:
    from app.routers.notas import router as notas_router
except ImportError:
    notas_router = None

app = FastAPI(title="MEI Online API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo os roteadores na API
app.include_router(auth_router, prefix="/auth", tags=["Autenticação"])

if clientes_router:
    app.include_router(clientes_router, prefix="/clientes", tags=["Clientes"])

if notas_router:
    app.include_router(notas_router, prefix="/notas", tags=["Notas"])

@app.get("/")
def read_root():
    return {"status": "online", "message": "API MEI Online rodando"}
