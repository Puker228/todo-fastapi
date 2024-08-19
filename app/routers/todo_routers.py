from fastapi import APIRouter, Depends
from typing import Annotated

from app.crud.todo_crud import ToDoCRUD
from app.schemas.todo_schemas import STodo, STodo_id, STodoById


router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo/")
async def new_todo(todo: Annotated[STodo, Depends()]):
    todo_id = await ToDoCRUD.add_one(todo)
    return todo


@router.get("/all-todos/")
async def all_todos() -> list[STodo]:
    todos = await ToDoCRUD.get_all()
    return todos


@router.put("/update-todo-by-id/")
async def update_todo(todo_id: int, new_data: Annotated[STodo, Depends()]) -> STodo:
    new_todo = await ToDoCRUD.update_one(todo_id=todo_id, data=new_data)
    return new_todo


@router.get("/get-one-by-id/")
async def get_one_todo(todo_id: int) -> STodoById:
    one_todo = await ToDoCRUD.get_one_by_id(todo_id)
    return one_todo
