# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API - Teste de Inicialização")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste conforme sua necessidade
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
