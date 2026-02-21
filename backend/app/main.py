import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from pydantic import BaseModel
from typing import List

# Configuração do Banco de Dados (Pega a variável que você colocou no Easypanel)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://meifiscal:An@Beatriz270172@meifiscal-db:5432/meifiscal")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- MODELOS DO BANCO DE DADOS ---
class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    documento = Column(String, unique=True) # CPF ou CNPJ
    email = Column(String)

class NotaFiscal(Base):
    __tablename__ = "notas_fiscais"
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    descricao = Column(String)
    data_emissao = Column(DateTime, default=datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

# Cria as tabelas no banco de dados automaticamente
Base.metadata.create_all(bind=engine)

# --- SCHEMAS PARA A API (Pydantic) ---
class ClienteCreate(BaseModel):
    nome: str
    documento: str
    email: str

class NotaCreate(BaseModel):
    valor: float
    descricao: str
    cliente_id: int

# --- INICIALIZAÇÃO DO FASTAPI ---
app = FastAPI(title="MEI Fiscal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência para o Banco de Dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROTAS (ENDPOINTS) ---

@app.get("/")
def root():
    return {"status": "MEI Fiscal API Online", "database": "Conectado"}

@app.post("/clientes/", response_model=ClienteCreate)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    novo_cliente = Cliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente

@app.get("/clientes/")
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@app.post("/notas/")
def emitir_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    nova_nota = NotaFiscal(**nota.dict())
    db.add(nova_nota)
    db.commit()
    db.refresh(nova_nota)
    return nova_nota

@app.get("/dashboard/")
def dashboard(db: Session = Depends(get_db)):
    total_faturado = db.query(NotaFiscal).with_entities(Float(NotaFiscal.valor)).all()
    soma = sum([n[0] for n in total_faturado])
    contagem = len(total_faturado)
    return {
        "faturamento_total": soma,
        "notas_emitidas": contagem,
        "limite_restante": 81000 - soma
    }
