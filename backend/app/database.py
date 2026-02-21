from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import logging

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:////tmp/test.db")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database")

engine = create_engine(
    DATABASE_URL,
    echo=True,  # DEBUG: mostra SQL no log, remova em produção
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

try:
    with engine.connect() as conn:
        logger.info("Conexão com banco de dados estabelecida com sucesso.")
except Exception as e:
    logger.exception("Erro ao conectar ao banco de dados: %s", e)
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
