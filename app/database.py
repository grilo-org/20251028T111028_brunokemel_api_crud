from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Detecta se está rodando no Render
is_render = os.getenv("RENDER") is not None

# Escolhe a URL do banco baseado no ambiente
if is_render:
    # No Render, usa SQLite
    database_url = settings.SQLITE_DATABASE_URL
    engine_kwargs = {
        "echo": settings.DEBUG,
        "connect_args": {"check_same_thread": False}  # Necessário para SQLite
    }
else:
    # Localmente, usa MySQL
    database_url = settings.DATABASE_URL
    engine_kwargs = {
        "echo": settings.DEBUG,
        "pool_pre_ping": True,
        "pool_recycle": 300
    }

# Criação do engine do banco de dados
engine = create_engine(database_url, **engine_kwargs)

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy
Base = declarative_base()


def get_db():
    """
    Dependency que fornece uma sessão do banco de dados
    
    Yields:
        Session: Sessão do SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

