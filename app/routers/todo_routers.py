from fastapi import APIRouter, HTTPException

from app.crud.todo_crud import ToDoCRUD
from app.schemas.todo_schemas import STodo, STodoResponce


router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo/")
async def add_new_todo(todo: STodo) -> STodoResponce:
    add_todo = await ToDoCRUD.add_one(todo)
    if not add_todo:
        raise HTTPException(status_code=400, detail="Unable to add todo item.")
    return add_todo


@router.get("/all-todos/")
async def all_todos() -> list[STodo]:
    todos = await ToDoCRUD.get_all()
    return todos


@router.put("/update-tod/{name}")
async def update_todo(name: str, new_data: STodo) -> STodoResponce:
    new_todo = await ToDoCRUD.update_one(post_name=name, data=new_data)
    return new_todo


@router.get("/get-one/{name}")
async def get_one_todo(name: str) -> STodoResponce:
    one_todo = await ToDoCRUD.get_one_by_id(name)
    return one_todo
