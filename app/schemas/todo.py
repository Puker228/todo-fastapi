from pydantic import BaseModel
from datetime import date


class STodo(BaseModel):
    name: str
    description: str | None = None
    end_date: date | None = None
    important: bool = False


class STodo_id(BaseModel):
    succes: bool = True
    todo_id: int
