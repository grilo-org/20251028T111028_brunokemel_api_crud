from datetime import datetime, timedelta
from typing import Optional, Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.config import settings

# Configuração de criptografia de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuração do OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha em texto plano corresponde ao hash
    
    Args:
        plain_password: Senha em texto plano
        hashed_password: Senha criptografada
        
    Returns:
        bool: True se as senhas coincidem
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Gera hash da senha
    
    Args:
        password: Senha em texto plano
        
    Returns:
        str: Hash da senha
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Cria token JWT de acesso
    
    Args:
        data: Dados a serem codificados no token
        expires_delta: Tempo de expiração do token
        
    Returns:
        str: Token JWT codificado
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception: HTTPException) -> Union[str, HTTPException]:
    """
    Verifica e decodifica o token JWT
    
    Args:
        token: Token JWT a ser verificado
        credentials_exception: Exceção a ser lançada em caso de erro
        
    Returns:
        str: Email do usuário se o token for válido
        
    Raises:
        HTTPException: Se o token for inválido ou expirado
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return email
    except JWTError:
        raise credentials_exception


def get_current_user_email(token: str = Depends(oauth2_scheme)) -> str:
    """
    Extrai o email do usuário atual do token JWT
    
    Args:
        token: Token JWT
        
    Returns:
        str: Email do usuário
        
    Raises:
        HTTPException: Se o token for inválido
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return verify_token(token, credentials_exception)


# Função para autenticação de usuário (será implementada quando necessário)
def authenticate_user(email: str, password: str) -> Optional[dict]:
    """
    Autentica um usuário com email e senha
    
    Args:
        email: Email do usuário
        password: Senha do usuário
        
    Returns:
        dict: Dados do usuário se autenticação for bem-sucedida
        None: Se autenticação falhar
    """
    # Esta função será implementada quando o sistema de autenticação for adicionado
    # Por enquanto, retorna None
    return None