# backend/app/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- app global esperado pelo Uvicorn (uvicorn app.main:app) ---
app = FastAPI(title="MEI Fiscal API")

# Habilita CORS para o frontend (troque "*" pelo domínio em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints simples de teste
@app.get("/", tags=["root"])
def read_root():
    return {"message": "MEI Fiscal API - OK"}

@app.get("/healthz", tags=["health"])
def healthz():
    return {"status": "ok"}

# Fallbacks úteis (remova quando ligar os routers reais)
@app.get("/dashboard/", tags=["fallback"])
def dashboard_fallback():
    return {"faturamento_mensal": 0.0, "notas_emitidas": 0, "limite_mei": 81000.0}

@app.get("/notas/", tags=["fallback"])
def notas_fallback():
    return []

# Execução local (não altera o comportamento quando rodado com uvicorn externamente)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, log_level="info")
