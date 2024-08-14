from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str | None] = mapped_column(default=None)
    full_name: Mapped[str | None] = mapped_column(default=None)
    disabled: Mapped[bool | None] = mapped_column(default=None)
