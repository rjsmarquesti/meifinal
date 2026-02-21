# backend/app/routers/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/test-auth")
def test_auth():
    return {"ok": True, "msg": "auth router funcionando"}
