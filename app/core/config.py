from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Configurações do banco de dados MySQL
    DB_USER: str = "root"
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_NAME: str = "cadastro_db"
    DB_PORT: int = 3306
    
    # Configurações de segurança JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Configurações da aplicação
    APP_NAME: str = "API de Usuários"
    DEBUG: bool = False
    
    class Config:
        env_file = "credenciais.env"  # carrega variáveis do arquivo credenciais.env
        case_sensitive = True

    @property
    def DATABASE_URL(self) -> str:
        """Retorna a URL de conexão com o banco MySQL"""
        return f"mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def SQLITE_DATABASE_URL(self) -> str:
        """Retorna a URL para banco SQLite (alternativa)"""
        return "sqlite:///./users.db"


# Instância global das configurações
settings = Settings()