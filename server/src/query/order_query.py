from sqlmodel import select

from ..database import AsyncSession
from ..database.order import Order, OrderCreate, OrderUpdate
from .base_query import BaseQuery


class OrderQuery(BaseQuery[Order, OrderCreate, OrderUpdate]):
    async def get_by_shopname(
        self, session: AsyncSession, shopname: str, offset: int = 0, limit: int = 100
    ) -> list[Order]:
        stmt = (
            select(Order).where(Order.shopname == shopname).offset(offset).limit(limit)
        )
        result = await session.execute(stmt)
        return result.scalars().all()


order = OrderQuery(Order)
