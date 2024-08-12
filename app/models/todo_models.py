from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date
from datetime import date

from app.database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    end_date: Mapped[date | None] = mapped_column(Date)
    important: Mapped[bool] = mapped_column(default=False)
