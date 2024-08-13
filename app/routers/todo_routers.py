from fastapi import APIRouter, Depends
from typing import Annotated

from app.crud.todo_crud import ToDoCRUD
from app.schemas.todo_schemas import STodo, STodo_id


router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo")
async def new_todo(todo: Annotated[STodo, Depends()]) -> STodo_id:
    todo_id = await ToDoCRUD.add_one(todo)
    return {"ok": True, "todo_id": todo_id}


@router.get("/all-todos")
async def all_todos() -> list[STodo]:
    todos = await ToDoCRUD.get_all()
    return todos
