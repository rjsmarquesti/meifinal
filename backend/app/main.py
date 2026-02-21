from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MEI Fiscal API")

# Habilita CORS para permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique o domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "MEI Fiscal API - OK"}

# Inclua aqui suas rotas manualmente, por exemplo:
# from app.routers import dashboard, notas
# app.include_router(dashboard.router)
# app.include_router(notas.router)

# Para testar, você pode criar rotas simples aqui até corrigir os routers
@app.get("/dashboard/")
def get_dashboard():
    return {"faturamento_mensal": 0, "notas_emitidas": 0, "limite_mei": 81000}

@app.get("/notas/")
def get_notas():
    return []

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info")
