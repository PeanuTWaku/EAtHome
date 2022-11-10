from typing import Any, Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select

ModelType = TypeVar("ModelType", bound=SQLModel)
ModelUpdate = TypeVar("ModelUpdate", bound=SQLModel)
ModelCreate = TypeVar("ModelCreate", bound=SQLModel)


class BaseQuery(Generic[ModelType, ModelCreate, ModelUpdate]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_by_id(
        self, session: AsyncSession, identifier: Any
    ) -> ModelType | None:
        return await session.get(self.model, identifier)

    async def get_batch(
        self, session: AsyncSession, offset: int = 0, limit: int = 100
    ) -> list[ModelType]:
        stmt = select(self.model).offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def create(self, session: AsyncSession, obj: ModelCreate) -> ModelType:
        db_obj = self.model.from_orm(obj)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        session: AsyncSession,
        db_obj: ModelType,
        obj: ModelUpdate | dict[str, Any],
    ) -> ModelType:
        update_data = obj if isinstance(obj, dict) else obj.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_obj, key, value)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(self, session: AsyncSession, identifier: Any) -> ModelType | None:
        obj = await session.get(self.model, identifier)

        if not obj:
            return None

        await session.delete(obj)
        await session.commit()
        return obj
