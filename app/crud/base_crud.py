from sqlalchemy import select, update, insert

from app.database import new_session


class BaseCRUD:
    model = None
    schema = None

    @classmethod
    async def add_one(cls, data: schema):
        async with new_session() as session:
            data_dict = data.model_dump()
            query = insert(cls.model).values(data_dict).returning(cls.model.id)
            result = await session.execute(query)
            await session.flush()
            await session.commit()

            new_id = result.scalar_one()

            # Извлекаем полную информацию о новой записи
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
            )

            result = await session.execute(query)
            await session.flush()
            await session.commit()
            return result

    @classmethod
    async def get_one_by_id(cls, post_id: int):
        async with new_session() as session:
            query = select(cls.model).filter_by(id=post_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()
