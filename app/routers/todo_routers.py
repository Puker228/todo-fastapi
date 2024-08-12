from fastapi import APIRouter, Depends
from typing import Annotated

from app.crud.todo_crud import ToDoCRUD
from app.schemas.todo_schemas import STodo, STodo_id


router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo", response_model=STodo_id)
async def new_todo(todo: Annotated[STodo, Depends()]):
    todo_id = await ToDoCRUD.add_one(todo)
    return {"ok": True, "todo_id": todo_id}


@router.get('/all-todos', response_model=list[STodo])
async def all_todos():
    todos = await ToDoCRUD.get_all()
    return {
        'data': todos
    }
