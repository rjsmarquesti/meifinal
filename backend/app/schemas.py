# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# --- CLIENTES ---
class ClienteBase(BaseModel):
    nome: str
    email: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    criado_em: Optional[datetime] = None

    class Config:
        orm_mode = True

# --- NOTAS ---
class NotaFiscalBase(BaseModel):
    descricao: str
    valor: float
    cliente_id: int

class NotaFiscalCreate(NotaFiscalBase):
    pass

class NotaFiscal(NotaFiscalBase):
    id: int
    data_emissao: Optional[datetime] = None
    criado_em: Optional[datetime] = None

    class Config:
        orm_mode = True

# --- USUÁRIO / AUTH ---
class UserCreate(BaseModel):
    nome: Optional[str] = None
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
