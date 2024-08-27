import time

from fastapi import APIRouter, HTTPException
from fastapi_cache.decorator import cache

from app.crud.todo import ToDoCRUD
from app.schemas.todo import STodo, STodoResponce

router = APIRouter(prefix="/todo", tags=["todos"])


@router.post("/new-todo/")
async def add_new_todo(todo: STodo) -> STodoResponce:
    add_todo = await ToDoCRUD.add_one(todo)
    if not add_todo:
        raise HTTPException(status_code=400, detail="Unable to add todo item.")
    return add_todo


@router.get("/all-todos/")
@cache(expire=60)
async def all_todos() -> list[STodoResponce]:
    time.sleep(10)  # test cache
    todos = await ToDoCRUD.get_all()
    return todos


@router.put("/update-tod/{name}")
async def update_todo(todo_id: int, new_data: STodo) -> STodoResponce:
    new_todo = await ToDoCRUD.update_one(post_id=todo_id, data=new_data)
    return new_todo


@router.get("/get-one/{name}")
async def get_one_todo(todo_id: int) -> STodoResponce:
    one_todo = await ToDoCRUD.get_one_by_id(todo_id)
    return one_todo
