from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Retorna lista de usuários"""
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    """Retorna um usuário específico por ID"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Cria um novo usuário"""
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user)
    db.commit()
    return{"mensagem": "Usuário deletado com sucesso"}

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
        # Checar duplicado email|cpf
    if db.query(models.User).filter(models.User.email == user.email, models.User.id != user_id).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado por outro usuário")

    if db.query(models.User).filter(models.User.cpf == user.cpf, models.User.id != user_id).first():
        raise HTTPException(status_code=400, detail="CPF já cadastrado por outro usuário")



# Atualizar os campos
    db_user.nome = user.nome
    db_user.email = user.email
    db_user.cpf = user.cpf
    db.commit()
    db.refresh(db_user)
    return db_user


