# backend/app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# --- Clientes ---
class ClienteBase(BaseModel):
    nome: str
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True

# --- Notas (NF-e / simples) ---
class NotaBase(BaseModel):
    cliente_id: int
    valor: float
    descricao: Optional[str] = None

class NotaCreate(NotaBase):
    pass

class Nota(NotaBase):
    id: int

    class Config:
        orm_mode = True

# --- Auth / Usuário (mínimo para endpoints de login/register) ---
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
