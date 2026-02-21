from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importação direta do router para garantir que o atributo seja encontrado
from app.routers.auth import router as auth_router

app = FastAPI(title="MEI Online API")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo o router de autenticação
app.include_router(auth_router, prefix="/auth", tags=["Autenticação"])

@app.get("/")
def read_root():
    return {"status": "online", "message": "API MEI Online rodando com sucesso"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
