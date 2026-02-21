# backend/app/schemas.py
from typing import Optional, List, Dict

# Tentar detectar Pydantic v2 (ConfigDict) ou v1 (Config.orm_mode)
try:
    # pydantic v2
    from pydantic import BaseModel, ConfigDict
    PydanticV2 = True
except Exception:
    # pydantic v1
    from pydantic import BaseModel
    PydanticV2 = False


# --- Usuários / Autenticação ---
if PydanticV2:
    class UserBase(BaseModel):
        username: str
        email: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

    class UserCreate(UserBase):
        password: str
        model_config = ConfigDict(from_attributes=True)

    class User(UserBase):
        id: int
        is_active: bool = True
        model_config = ConfigDict(from_attributes=True)

    class Token(BaseModel):
        access_token: str
        token_type: str
        model_config = ConfigDict(from_attributes=True)

    class TokenData(BaseModel):
        username: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

    # --- Clientes ---
    class ClienteBase(BaseModel):
        nome: str
        email: Optional[str] = None
        cpf_cnpj: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

    class ClienteCreate(ClienteBase):
        model_config = ConfigDict(from_attributes=True)

    class Cliente(ClienteBase):
        id: int
        model_config = ConfigDict(from_attributes=True)

    # --- Notas Fiscais ---
    class NotaFiscalBase(BaseModel):
        cliente_id: int
        valor_total: float
        observacoes: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

    class NotaFiscalCreate(NotaFiscalBase):
        model_config = ConfigDict(from_attributes=True)

    class NotaFiscal(NotaFiscalBase):
        id: int
        numero: Optional[str] = None
        data_emissao: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

else:
    class UserBase(BaseModel):
        username: str
        email: Optional[str] = None

        class Config:
            orm_mode = True

    class UserCreate(UserBase):
        password: str

        class Config:
            orm_mode = True

    class User(UserBase):
        id: int
        is_active: bool = True

        class Config:
            orm_mode = True

    class Token(BaseModel):
        access_token: str
        token_type: str

        class Config:
            orm_mode = True

    class TokenData(BaseModel):
        username: Optional[str] = None

        class Config:
            orm_mode = True

    # Clientes
    class ClienteBase(BaseModel):
        nome: str
        email: Optional[str] = None
        cpf_cnpj: Optional[str] = None

        class Config:
            orm_mode = True

    class ClienteCreate(ClienteBase):
        class Config:
            orm_mode = True

    class Cliente(ClienteBase):
        id: int

        class Config:
            orm_mode = True

    # Notas
    class NotaFiscalBase(BaseModel):
        cliente_id: int
        valor_total: float
        observacoes: Optional[str] = None

        class Config:
            orm_mode = True

    class NotaFiscalCreate(NotaFiscalBase):
        class Config:
            orm_mode = True

    class NotaFiscal(NotaFiscalBase):
        id: int
        numero: Optional[str] = None
        data_emissao: Optional[str] = None

        class Config:
            orm_mode = True
