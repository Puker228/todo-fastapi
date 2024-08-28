from datetime import date

from pydantic import BaseModel, ConfigDict


class STodo(BaseModel):
    todo_name: str
    description: str | None = None
    end_date: date | None = None
    important: bool = False

    model_config = ConfigDict(from_attributes=True)


class STodoResponce(BaseModel):
    id: int
    todo_name: str
    description: str | None = None
    end_date: date | None = None
    important: bool = False

    model_config = ConfigDict(from_attributes=True)
