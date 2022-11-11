from sqlmodel import select

from ..database import AsyncSession
from ..database.product import Product, ProductCreate, ProductUpdate
from .base_query import BaseQuery


class ProductQuery(BaseQuery[Product, ProductCreate, ProductUpdate]):
    async def get_by_shopname(
        self, session: AsyncSession, shopname: str, offset: int = 0, limit: int = 100
    ) -> list[Product]:
        stmt = (
            select(Product)
            .where(Product.shopname == shopname)
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(stmt)
        return result.scalars().all()


product = ProductQuery(Product)
