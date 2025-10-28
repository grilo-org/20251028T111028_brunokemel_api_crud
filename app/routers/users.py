from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

# Dependência de sessão com o banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Criar usuário
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


# ✅ Listar todos os usuários
@router.get("/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


# ✅ Obter usuário por ID
@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user


# ✅ Atualizar usuário
@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


# ✅ Deletar usuário
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)