from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging

from app import models, schemas
from app.database import get_db

logger = logging.getLogger("clientes")
logger.setLevel(logging.INFO)

router = APIRouter()

@router.get("/", response_model=List[schemas.Cliente])
def listar_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(models.Cliente).offset(skip).limit(limit).all()
    except Exception as e:
        logger.exception("Erro ao listar clientes: %s", e)
        raise HTTPException(status_code=500, detail="Erro interno ao listar clientes")

@router.post("/", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    try:
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
    except Exception as e:
        logger.exception("Erro ao criar cliente: %s", e)
        try:
            db.rollback()
        except Exception:
            logger.exception("Rollback falhou")
        raise HTTPException(status_code=500, detail="Erro interno ao criar cliente")

@router.get("/{cliente_id}", response_model=schemas.Cliente)
def obter_cliente(cliente_id: int, db: Session = Depends(get_db)):
    try:
        c = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
        if not c:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return c
    except Exception as e:
        logger.exception("Erro ao obter cliente %s: %s", cliente_id, e)
        raise HTTPException(status_code=500, detail="Erro interno ao obter cliente")
