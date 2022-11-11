from fastapi import APIRouter, Depends, HTTPException, status

from src import query
from src.auth import manager
from src.database import AsyncSession, get_session
from src.database.shop import ShopCreate, ShopRead, ShopUpdate
from src.database.user import User

router = APIRouter()


@router.get("/", response_model=list[ShopRead])
async def read_shops(
    session: AsyncSession = Depends(get_session),
    *,
    offset: int = 0,
    limit: int = 100,
    category: str | None = None,
    latitude: float,
    longitude: float,
    distance: int,
):
    return await query.shop.get_by_filters(
        session,
        category=category,
        latitude=latitude,
        longitude=longitude,
        offset=offset,
        limit=limit,
        distance=distance,
    )


@router.get("/my", response_model=ShopRead)
async def get_my_shop(owner: User = Depends(manager)):
    if not owner.shop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not have a shop!"
        )
    return owner.shop


@router.get("/{shopname}")
async def read_shop(session: AsyncSession = Depends(get_session), *, shopname: str):
    return await query.shop.get_by_id(session, shopname)


@router.post("/", response_model=ShopRead, status_code=status.HTTP_201_CREATED)
async def create_shop(
    session: AsyncSession = Depends(get_session),
    owner: User = Depends(manager),
    *,
    shop: ShopCreate,
):
    if owner.shop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already has one shop!"
        )
    return await query.shop.create(session, shop)


@router.patch("/my", response_model=ShopRead)
async def update_my(
    session: AsyncSession = Depends(get_session),
    owner: User = Depends(manager),
    *,
    update: ShopUpdate,
):
    if not owner.shop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not have a shop!"
        )

    return await query.shop.update(session, owner.shop, update)
