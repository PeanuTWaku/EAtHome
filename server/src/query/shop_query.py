from sqlmodel import select

from ..database import AsyncSession
from ..database.shop import Shop, ShopCreate, ShopUpdate
from .base_query import BaseQuery


class ShopQuery(BaseQuery[Shop, ShopCreate, ShopUpdate]):
    async def get_by_category(
        self, session: AsyncSession, category: str, offset: int = 0, limit: int = 100
    ) -> list[Shop]:
        stmt = select(Shop).where(Shop.category == category).offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def get_by_distance(
        self, session: AsyncSession, distance: int, offset: int = 0, limit: int = 100
    ) -> list[Shop]:
        ...


shop = ShopQuery(Shop)
