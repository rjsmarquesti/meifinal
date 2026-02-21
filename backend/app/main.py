from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importamos apenas os que preenchemos acima
from app.routers import dashboard, clientes, notas

app = FastAPI(title="MEI Fiscal API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas principais
app.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
app.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
app.include_router(notas.router, prefix="/notas", tags=["notas"])

@app.get("/")
def read_root():
    return {"message": "API Online"}
