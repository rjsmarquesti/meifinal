from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ── Cliente ──────────────────────────────────────────
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
        from_attributes = True

# ── Nota Fiscal ──────────────────────────────────────
class NotaFiscalBase(BaseModel):
    descricao: str
    valor: float
    cliente_id: int
    data_emissao: Optional[datetime] = None

class NotaFiscalCreate(NotaFiscalBase):
    pass

class NotaFiscal(NotaFiscalBase):
    id: int
    criado_em: Optional[datetime] = None

    class Config:
        from_attributes = True

# ── Dashboard ─────────────────────────────────────────
class DashboardStats(BaseModel):
    faturamento_mensal: float = 0.0
    notas_emitidas: int = 0
    limite_mei: float = 81000.0
    percentual_utilizado: float = 0.0
