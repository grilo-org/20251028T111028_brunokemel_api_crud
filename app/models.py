from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), unique=True,  index=True, nullable=False)