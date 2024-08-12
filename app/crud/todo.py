from app.schemas.todo import STodo
from app.database import new_session
from app.models.todo import ToDo


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
