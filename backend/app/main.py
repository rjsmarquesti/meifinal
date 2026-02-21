# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pkgutil
import importlib
import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI(title="MEI Fiscal API")

# CORS - permitir chamadas do frontend
# Em produção, prefira colocar somente o domínio do frontend em allow_origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Healthcheck / root
@app.get("/", tags=["root"])
def read_root():
    return {"message": "MEI Fiscal API - OK"}

# Tenta automaticamente incluir routers em app/routers/*
try:
    import app.routers as routers_pkg

    for finder, name, ispkg in pkgutil.iter_modules(routers_pkg.__path__):
        module_name = f"{routers_pkg.__name__}.{name}"
        try:
            mod = importlib.import_module(module_name)
            if hasattr(mod, "router"):
                app.include_router(getattr(mod, "router"))
                logger.info(f"Incluindo router: {module_name}.router")
            elif hasattr(mod, "api_router"):
                app.include_router(getattr(mod, "api_router"))
                logger.info(f"Incluindo router: {module_name}.api_router")
            else:
                logger.info(f"Módulo encontrado mas sem 'router' exportado: {module_name}")
        except Exception as e:
            logger.exception(f"Erro ao importar {module_name}: {e}")
except ModuleNotFoundError:
    logger.info("Pacote app.routers não encontrado — nenhum router foi incluído automaticamente.")
except Exception as e:
    logger.exception(f"Erro ao carregar routers: {e}")

@app.get("/healthz", tags=["health"])
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info")
