from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import clientes, notas, dashboard

app = FastAPI(title="MEI Fiscal - API Principal")

# Configuração de CORS para o seu Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, você pode trocar pelo seu domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas dos outros arquivos
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(notas.router, prefix="/notas", tags=["Notas"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "API MEI Fiscal Online"}
