from sqlmodel import select

from ..database import AsyncSession
from ..database.shop import Shop, ShopCreate, ShopUpdate
from .base_query import BaseQuery


class ShopQuery(BaseQuery[Shop, ShopCreate, ShopUpdate]):
    async def get_by_filters(
        self,
        session: AsyncSession,
        *,
        category: str | None = None,
        latitude: float,
        longitude: float,
        distance: int,
        offset: int = 0,
        limit: int = 100,
    ) -> list[Shop]:

        if category is not None:
            stmt = (
                select(Shop)
                .where(Shop.category == category)
                .offset(offset)
                .limit(limit)
            )
        result = await session.execute(stmt)
        return result.scalars().all()


shop = ShopQuery(Shop)
