from sqlalchemy import func
from sqlmodel import select

from ..database import AsyncSession
from ..database.shop import Shop, ShopCreate, ShopUpdate
from .base_query import BaseQuery

EARTH_RADIUS = 6371


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

        distance_stmt = (
            2
            * EARTH_RADIUS
            * func.asin(
                func.sqrt(
                    0.5
                    - func.cos(func.radians(latitude - Shop.latitude)) / 2
                    + func.cos(func.radians(Shop.latitude))
                    * func.cos(func.radians(latitude))
                    * (1 - func.cos(func.radians(longitude - Shop.longitude)))
                    / 2
                )
            )
        )

        if category is not None:
            stmt = (
                select(Shop)
                .where(
                    Shop.category == category,
                    distance_stmt <= distance,
                )
                .offset(offset)
                .limit(limit)
            )
        else:
            stmt = (
                select(Shop)
                .where(distance_stmt <= distance)
                .offset(offset)
                .limit(limit)
            )

        result = await session.execute(stmt)
        return result.scalars().all()


shop = ShopQuery(Shop)
