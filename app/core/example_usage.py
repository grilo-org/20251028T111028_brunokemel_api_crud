"""
Exemplo de uso das configurações e segurança do projeto

Este arquivo demonstra como usar as funcionalidades implementadas
nos módulos config.py e security.py
"""

from app.core.config import settings
from app.core.security import (
    create_access_token,
    get_password_hash,
    verify_password,
    get_current_user_email
)
from datetime import timedelta

def exemplo_configuracao():
    """Exemplo de uso das configurações"""
    print("=== Exemplo de Configurações ===")
    print(f"Nome da aplicação: {settings.APP_NAME}")
    print(f"Host do banco: {settings.DB_HOST}")
    print(f"Nome do banco: {settings.DB_NAME}")
    print(f"URL do banco: {settings.DATABASE_URL}")
    print(f"Algoritmo JWT: {settings.ALGORITHM}")
    print(f"Tempo de expiração do token: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} minutos")
    print(f"Modo debug: {settings.DEBUG}")


def exemplo_seguranca():
    """Exemplo de uso das funções de segurança"""
    print("\n=== Exemplo de Segurança ===")
    
    # Exemplo de hash de senha
    senha = "minhasenha123"
    hash_senha = get_password_hash(senha)
    print(f"Senha original: {senha}")
    print(f"Hash da senha: {hash_senha}")
    
    # Verificação de senha
    senha_correta = verify_password(senha, hash_senha)
    senha_incorreta = verify_password("senhaerrada", hash_senha)
    print(f"Senha correta verifica: {senha_correta}")
    print(f"Senha incorreta verifica: {senha_incorreta}")
    
    # Criação de token JWT
    dados_usuario = {"sub": "usuario@email.com", "id": 1}
    token = create_access_token(dados_usuario)
    print(f"Token JWT criado: {token[:50]}...")
    
    # Token com tempo de expiração personalizado
    token_custom = create_access_token(
        dados_usuario, 
        expires_delta=timedelta(hours=1)
    )
    print(f"Token com 1 hora de expiração: {token_custom[:50]}...")


def exemplo_integracao():
    """Exemplo de integração com FastAPI"""
    print("\n=== Exemplo de Integração FastAPI ===")
    print("Para usar em rotas do FastAPI:")
    print("""
from fastapi import APIRouter, Depends
from app.core.security import get_current_user_email

router = APIRouter()

@router.get("/protected")
async def rota_protegida(current_user_email: str = Depends(get_current_user_email)):
    return {"message": f"Olá {current_user_email}, você está autenticado!"}
    """)


if __name__ == "__main__":
    exemplo_configuracao()
    exemplo_seguranca()
    exemplo_integracao()
