from sqlalchemy import select, update

from app.schemas.todo_schemas import STodo
from app.database import new_session
from app.models.todo_models import ToDo


class ToDoCRUD:
    @classmethod
    async def add_one(cls, data: STodo):
        async with new_session() as session:
            todo_dict = data.model_dump()

            todo = ToDo(**todo_dict)
            session.add(todo)

            await session.flush()
            await session.commit()
            return todo.id

    @classmethod
    async def get_all(cls) -> list[STodo]:
        async with new_session() as session:
            query = select(ToDo)
            result = await session.execute(query)
            todo_models = result.scalars().all()
            todo_schema = [
                STodo.model_validate(todo_model) for todo_model in todo_models
            ]
            return todo_schema
        

    @classmethod
    async def update_one(cls, todo_id: int, data: STodo) -> None:
        async with new_session() as session:
            query = update(ToDo).where(ToDo.id == todo_id).values(data.model_dump())
            await session.execute(query)
            await session.commit()
            return data