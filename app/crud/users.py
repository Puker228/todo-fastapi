from sqlalchemy import select, update, insert

from app.database import new_session
from app.models.users import Users


class UsersCRUD:
    model = Users

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            res = await session.execute(query)
            return res.scalar_one_or_none()

    @classmethod
    async def add_one(cls, **data):
        async with new_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
