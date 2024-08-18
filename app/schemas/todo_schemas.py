from pydantic import BaseModel, ConfigDict
from datetime import date


class STodo(BaseModel):
    name: str
    description: str | None = None
    end_date: date | None = None
    important: bool = False

    model_config = ConfigDict(from_attributes=True)


class STodo_id(BaseModel):
    succes: bool = True
    todo_id: int


class STodoById(STodo):
    id: int
