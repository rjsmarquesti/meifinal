# backend/app/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.database import engine
from app.routers import auth, clientes, notas

# Cria tabelas automaticamente (somente se NÃO usar Alembic)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MEI Fiscal - API Principal")

# Ajuste o CORS para o seu frontend (substitua pelo domínio real em produção)
FRONTEND_URL = os.getenv("FRONTEND_URL", "*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL] if FRONTEND_URL != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui os routers
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(notas.router, prefix="/notas", tags=["Notas"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "API MEI Fiscal Online"}
