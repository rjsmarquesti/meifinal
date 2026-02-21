from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=True, index=True)
    cpf = Column(String, nullable=True, index=True)
    telefone = Column(String, nullable=True)

    notas = relationship("Nota", back_populates="cliente")

class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(String, nullable=True)

    cliente = relationship("Cliente", back_populates="notas")
