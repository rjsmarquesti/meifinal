# backend/app/routers/notas.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db
# opcional: proteger rotas -> from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[schemas.NotaFiscal])
def listar_notas(db: Session = Depends(get_db)):
    return db.query(models.NotaFiscal).all()

@router.post("/", response_model=schemas.NotaFiscal, status_code=status.HTTP_201_CREATED)
def emitir_nota(nota: schemas.NotaFiscalCreate, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == nota.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado")
    db_nota = models.NotaFiscal(**nota.dict())
    db.add(db_nota)
    try:
        db.commit()
        db.refresh(db_nota)
        return db_nota
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Erro ao emitir nota: {str(e)}")

@router.delete("/{nota_id}", status_code=status.HTTP_200_OK)
def excluir_nota(nota_id: int, db: Session = Depends(get_db)):
    db_nota = db.query(models.NotaFiscal).filter(models.NotaFiscal.id == nota_id).first()
    if not db_nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    db.delete(db_nota)
    db.commit()
    return {"message": "Nota excluída"}
