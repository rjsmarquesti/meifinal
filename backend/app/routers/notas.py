from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from typing import List

router = APIRouter()

@router.get("/", response_model=List[schemas.NotaFiscal])
def listar_notas(db: Session = Depends(database.get_db)):
    return db.query(models.NotaFiscal).all()

@router.post("/", response_model=schemas.NotaFiscal)
def emitir_nota(nota: schemas.NotaFiscalCreate, db: Session = Depends(database.get_db)):
    # Verifica se o cliente existe antes de emitir a nota
    cliente = db.query(models.Cliente).filter(models.Cliente.id == nota.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=400, detail="Cliente não encontrado")
    
    db_nota = models.NotaFiscal(**nota.dict())
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return db_nota

@router.delete("/{nota_id}")
def excluir_nota(nota_id: int, db: Session = Depends(database.get_db)):
    db_nota = db.query(models.NotaFiscal).filter(models.NotaFiscal.id == nota_id).first()
    if not db_nota:
        raise HTTPException(status_code=404, detail="Nota não encontrada")
    db.delete(db_nota)
    db.commit()
    return {"message": "Nota excluída"}
