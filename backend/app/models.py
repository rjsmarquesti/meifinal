# backend/app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base  # importa do package app

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=True)
    cpf_cnpj = Column(String, nullable=True)
    telefone = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    notas = relationship("NotaFiscal", back_populates="cliente")


class NotaFiscal(Base):
    __tablename__ = "notas_fiscais"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    data_emissao = Column(DateTime, default=datetime.utcnow)
    criado_em = Column(DateTime, default=datetime.utcnow)

    cliente = relationship("Cliente", back_populates="notas")


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)  # HASH da senha
