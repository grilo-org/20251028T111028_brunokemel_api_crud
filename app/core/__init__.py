"""
Módulo core da aplicação FastAPI

Este módulo contém as configurações principais da aplicação,
incluindo configurações de banco de dados, segurança e autenticação.
"""

from .config import settings
from .security import (
    verify_password,
    get_password_hash,
    create_access_token,
    verify_token,
    get_current_user_email,
    authenticate_user,
    oauth2_scheme,
    pwd_context
)

__all__ = [
    "settings",
    "verify_password",
    "get_password_hash", 
    "create_access_token",
    "verify_token",
    "get_current_user_email",
    "authenticate_user",
    "oauth2_scheme",
    "pwd_context"
]
