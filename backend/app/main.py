from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from . import models, schemas, database

# Cria as tabelas no banco de dados ao iniciar
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="MEI Fiscal API")

# CORS: permitir o domínio do FRONTEND e (opcional) o domínio do BACKEND
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "MEI Fiscal API está online"}

@app.post("/clientes/", response_model=schemas.Cliente)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(database.get_db)):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.get("/clientes/", response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(database.get_db)):
    return db.query(models.Cliente).all()

@app.post("/notas/", response_model=schemas.NotaFiscal)
def emitir_nota(nota: schemas.NotaFiscalCreate, db: Session = Depends(database.get_db)):
    db_nota = models.NotaFiscal(**nota.dict())
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return db_nota

@app.get("/notas/", response_model=List[schemas.NotaFiscal])
def listar_notas(db: Session = Depends(database.get_db)):
    return db.query(models.NotaFiscal).all()

@app.get("/dashboard/")
def get_dashboard(db: Session = Depends(database.get_db)):
    faturamento = db.query(func.sum(models.NotaFiscal.valor)).scalar() or 0
    notas_count = db.query(models.NotaFiscal).count()
    return {
        "faturamento_mensal": float(faturamento),
        "notas_emitidas": notas_count,
        "limite_mei": 81000,
        @app.delete("/clientes/{cliente_id}")
def excluir_cliente(cliente_id: int, db: Session = Depends(database.get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
        return {"message": "Cliente excluído"}
    return {"error": "Cliente não encontrado"}
    }
