from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    cpf: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

class Config:
    from_attributes = True
