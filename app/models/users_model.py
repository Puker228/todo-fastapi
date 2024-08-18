from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, Text
from datetime import date
from pydantic import EmailStr

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
