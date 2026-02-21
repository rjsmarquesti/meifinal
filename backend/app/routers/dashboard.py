from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_dashboard():
    # Valores iniciais para o dashboard não dar erro no front
    return {
        "faturamento_mensal": 0.0,
        "notas_emitidas": 0,
        "limite_mei": 81000.0
    }
