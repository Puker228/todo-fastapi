from sqlalchemy import select, update, insert
from sqlalchemy.exc import NoResultFound

from app.database import new_session


class BaseCRUD:
    model = None

    @classmethod
    async def add_one(cls, data):
        async with new_session() as session:
            data_dict = data.model_dump()
            query = insert(cls.model).values(data_dict).returning(cls.model.id)
            result = await session.execute(query)
            await session.flush()
            await session.commit()

            # вывод новых данных
            new_id = result.scalar_one()

            stmt = select(cls.model).where(cls.model.id == new_id)
            result = await session.execute(stmt)
            new_post = result.scalar_one()

            return new_post

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
                .returning(cls.model.id)
            )

            result = await session.execute(query)
            await session.flush()
            await session.commit()

            # вывод обновленных данных
            new_id = result.scalar_one()

            stmt = select(cls.model).where(cls.model.id == new_id)
            result = await session.execute(stmt)
            new_post = result.scalar_one()

            return new_post

    @classmethod
    async def get_one_by_id(cls, post_id: int):
        async with new_session() as session:
            try:
                query = select(cls.model).filter_by(id=post_id)
                result = await session.execute(query)
                return result.scalar_one()
            except NoResultFound:
                return None
