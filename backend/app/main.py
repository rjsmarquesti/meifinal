from fastapi import FastAPI
import logging

from app.database import engine, Base
from app.routers import clientes, notas, auth  # supondo que auth.py exista

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("startup")

app = FastAPI(title="MEI Online API")

@app.on_event("startup")
def on_startup():
    try:
        logger.info("Criando/verificando tabelas...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tabelas criadas/verificadas com sucesso.")
    except Exception as e:
        logger.exception("Erro ao criar/verificar tabelas: %s", e)

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(notas.router, prefix="/notas", tags=["Notas"])

@app.get("/")
def read_root():
    return {"status": "online", "message": "API MEI Online rodando"}
