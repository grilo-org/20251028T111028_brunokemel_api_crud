from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users
from app import models, database

models.Base.metadata.create_all(bind=database.engine)  # Remove todas as tabelas (apenas para desenvolvimento)

# Cria as tabelas do banco de dados
models.Base.metadata.create_all(bind=database.engine)

# Cria a aplicação FastAPI
app = FastAPI(title="API de Usuários com FastAPI e SQLAlchemy")

# 🔥 ADICIONE ESTA CONFIGURAÇÃO DE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URLs do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui rotas de usuários
app.include_router(users.router, prefix="/users", tags=["users"])

# Executa a aplicação
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))  # Usa a porta do Render ou 8000 local
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)