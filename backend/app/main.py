import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models, database
from app.routers import auth, clientes, notas

# Cria as tabelas no banco de dados automaticamente
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="MEI Fiscal - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(notas.router, prefix="/notas", tags=["Notas"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "API Online"}
