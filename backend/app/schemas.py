# backend/app/schemas.py
from typing import Optional, List
try:
    # pydantic v2
    from pydantic import BaseModel, ConfigDict
    PydanticV2 = True
except Exception:
    # pydantic v1
    from pydantic import BaseModel
    PydanticV2 = False


if PydanticV2:
    class Cliente(BaseModel):
        id: int
        nome: str
        email: Optional[str] = None
        model_config = ConfigDict(from_attributes=True)

    class NotaCreate(BaseModel):
        cliente_id: int
        itens: List[dict]  # adapte conforme sua estrutura
        total: float
        model_config = ConfigDict(from_attributes=True)

    class NotaFiscal(BaseModel):
        id: int
        numero: str
        cliente_id: int
        total: float
        model_config = ConfigDict(from_attributes=True)

else:
    class Cliente(BaseModel):
        id: int
        nome: str
        email: Optional[str] = None

        class Config:
            orm_mode = True

    class NotaCreate(BaseModel):
        cliente_id: int
        itens: List[dict]
        total: float

        class Config:
            orm_mode = True

    class NotaFiscal(BaseModel):
        id: int
        numero: str
        cliente_id: int
        total: float

        class Config:
            orm_mode = True
