from fastapi import APIRouter, Depends
from typing import Annotated

from app.crud.todo import ToDoCRUD
from app.schemas.todo import STodo, STodo_id


router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo")
async def new_todo(todo: Annotated[STodo, Depends()]):
    todo_id = await ToDoCRUD.add_one(todo)
    return {"ok": True, "todo_id": todo_id}
