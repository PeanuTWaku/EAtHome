from fastapi import APIRouter, Depends

from src import query
from src.auth import manager
from src.database import AsyncSession, get_session
from src.database.order import OrderCreate, OrderRead, OrderProductRead
from src.database.user import User

router = APIRouter()


@router.get("/", response_model=list[OrderRead])
async def read_shop_orders(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(manager),
    offset: int = 0,
    limit: int = 100,
):
    return await query.order.get_by_shopname(session, user.shop.name, offset, limit)

@router.get("/my", response_model=list[OrderProductRead])
async def read_my_orders(
    user: User = Depends(manager),
    offset: int = 0,
    limit: int = 100,
):
    products = user.orders
    response = OrderProductRead(**user.orders, products=)
    return user.orders
