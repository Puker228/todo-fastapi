from sqlalchemy import select, update, insert

from app.database import new_session


class BaseCRUD:
    model = None

    @classmethod
    async def add_one(cls, data):
        async with new_session() as session:
            data_dict = data.model_dump()
            query = insert(cls.model).values(**data_dict)
            result = await session.execute(query)
            await session.flush()
            await session.commit()

            return result.scalars().all()

    @classmethod
    async def get_all(cls, **filter_by):
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def update_one(cls, post_id: int, data):
        async with new_session() as session:
            query = (
                update(cls.model)
                .where(cls.model.id == post_id)
                .values(data.model_dump())
            )

            await session.execute(query)
            await session.commit()
            return data

    @classmethod
    async def get_one_by_id(cls, post_id: int):
        async with new_session() as session:
            query = select(cls.model).filter_by(id=post_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()
