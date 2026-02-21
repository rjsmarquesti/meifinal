from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class NotaBase(BaseModel):
    valor: float
    descricao: str
    cliente_id: int

class NotaCreate(NotaBase):
    pass

class Nota(NotaBase):
    id: int
    data_emissao: datetime
    class Config:
        from_attributes = True

class ClienteBase(BaseModel):
    nome: str
    cpf_cnpj: str
    email: Optional[str] = None
    telefone: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    notas: List[Nota] = []
    class Config:
        from_attributes = True
