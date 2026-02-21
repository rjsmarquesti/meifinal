from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_clientes():
    return []

@router.post("/")
async def criar_cliente(cliente: dict):
    return {"message": "Cliente recebido", "data": cliente}
