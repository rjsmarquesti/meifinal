from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging

from app import models, schemas
from app.database import get_db

logger = logging.getLogger("notas")
logger.setLevel(logging.INFO)

router = APIRouter()

@router.get("/", response_model=List[schemas.Nota])
def listar_notas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(models.Nota).offset(skip).limit(limit).all()
    except Exception as e:
        logger.exception("Erro ao listar notas: %s", e)
        raise HTTPException(status_code=500, detail="Erro interno ao listar notas")

@router.post("/", response_model=schemas.Nota, status_code=status.HTTP_201_CREATED)
def emitir_nota(nota: schemas.NotaCreate, db: Session = Depends(get_db)):
    try:
        # Verifica se cliente existe
        cliente = db.query(models.Cliente).filter(models.Cliente.id == nota.cliente_id).first()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado para emitir nota")

        novo = models.Nota(
            cliente_id=nota.cliente_id,
            valor=nota.valor,
            descricao=nota.descricao,
        )
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo
    except Exception as e:
        logger.exception("Erro ao emitir nota: %s", e)
        try:
            db.rollback()
        except Exception:
            logger.exception("Rollback falhou")
        raise HTTPException(status_code=500, detail="Erro interno ao emitir nota")

@router.get("/{nota_id}", response_model=schemas.Nota)
def obter_nota(nota_id: int, db: Session = Depends(get_db)):
    try:
        n = db.query(models.Nota).filter(models.Nota.id == nota_id).first()
        if not n:
            raise HTTPException(status_code=404, detail="Nota não encontrada")
        return n
    except Exception as e:
        logger.exception("Erro ao obter nota %s: %s", nota_id, e)
        raise HTTPException(status_code=500, detail="Erro interno ao obter nota")
