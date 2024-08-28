from datetime import date

from sqlalchemy import Date, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ToDo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    todo_name: Mapped[str]
    description: Mapped[str | None] = mapped_column(Text)
    end_date: Mapped[date | None] = mapped_column(Date)
    important: Mapped[bool] = mapped_column(default=False)
