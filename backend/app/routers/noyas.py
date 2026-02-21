from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/")
async def listar_notas():
    return []

@router.post("/")
async def emitir_nota(nota: dict):
    return {"message": "Nota recebida", "data": nota}
