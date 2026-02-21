# Rotas Auth
from fastapi import APIRouter

# Esta é a variável que o main.py está procurando!
router = APIRouter()

@router.get("/test-auth")
def test_auth():
    return {"ok": True, "msg": "O roteador de autenticação foi encontrado!"}

# Depois colocaremos aqui as rotas de Login e Cadastro reais
