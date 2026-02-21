from sqlalchemy.orm import Session
from . import models, schemas

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_notas(db: Session):
    return db.query(models.Nota).all()

def create_nota(db: Session, nota: schemas.NotaCreate):
    db_nota = models.Nota(**nota.dict())
    db.add(db_nota)
    db.commit()
    db.refresh(db_nota)
    return db_nota
