from typing import Optional, List, Dict
from pydantic import BaseModel, ConfigDict

# --- CONFIGURAÇÃO PARA USUÁRIOS (LOGIN E CADASTRO) ---
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- CONFIGURAÇÃO PARA CLIENTES ---
class ClienteBase(BaseModel):
    nome: str
    email: Optional[str] = None
    cpf_cnpj: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- CONFIGURAÇÃO PARA NOTAS FISCAIS ---
class NotaFiscalBase(BaseModel):
    cliente_id: int
    valor_total: float
    observacoes: Optional[str] = None

class NotaFiscalCreate(NotaFiscalBase):
    pass

class NotaFiscal(NotaFiscalBase):
    id: int
    numero: Optional[str] = None
    data_emissao: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
