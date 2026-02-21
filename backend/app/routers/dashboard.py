# backend/app/routers/dashboard.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_dashboard():
    return {"faturamento_mensal": 1000, "notas_emitidas": 5, "limite_mei": 81000}
