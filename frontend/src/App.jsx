import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Criação do app global
app = FastAPI(title="MEI Fiscal API")

# Configuração de CORS para o frontend conseguir conectar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota de teste de saúde
@app.get("/")
def read_root():
    return {"status": "online", "message": "MEI Fiscal API"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

# Rotas temporárias para o frontend não dar erro de conexão
@app.get("/dashboard/")
def dashboard_fallback():
    return {
        "faturamento_mensal": 0.0, 
        "notas_emitidas": 0, 
        "limite_mei": 81000.0
    }

@app.get("/notas/")
def notas_fallback():
    return []

@app.get("/clientes/")
def clientes_fallback():
    return []
