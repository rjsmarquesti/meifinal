# backend/app/routers/clientes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db
# opcional: proteger rotas -> from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(models.Cliente).all()

@router.post("/", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    try:
        db.commit()
        db.refresh(db_cliente)
        return db_cliente
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar cliente: {e}")

@router.delete("/{cliente_id}", status_code=status.HTTP_200_OK)
def excluir_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(db_cliente)
    db.commit()
    return {"message": "Cliente excluído"}
