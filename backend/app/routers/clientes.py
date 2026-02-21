from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal, engine

# Garante que as tabelas existam (apenas para desenvolvimento rápido)
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Cliente])
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

@router.post("/", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    novo = models.Cliente(
        nome=cliente.nome,
        email=cliente.email,
        cpf=cliente.cpf,
        telefone=cliente.telefone,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/{cliente_id}", response_model=schemas.Cliente)
def obter_cliente(cliente_id: int, db: Session = Depends(get_db)):
    c = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not c:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return c
