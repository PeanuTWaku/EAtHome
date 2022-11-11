from fastapi import APIRouter, Depends, HTTPException, status
from src import query
from src.auth import manager
from src.database import AsyncSession, get_session
from src.database.user import User, UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.get("/", response_model=list[UserRead], dependencies=[Depends(manager)])
async def read_users(
    session: AsyncSession = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return await query.user.get_batch(session, offset, limit)


@router.get("/me", response_model=UserRead)
async def who_am_i(user: User = Depends(manager)):
    return user


@router.get("/{account}", response_model=UserRead, dependencies=[Depends(manager)])
async def read_user(session: AsyncSession = Depends(get_session), *, account: str):
    result = await query.user.get_by_id(session, account)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {account} does not exist",
        )
    return result


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def sign_up_user(
    session: AsyncSession = Depends(get_session), *, user: UserCreate
):
    if (created_user := await query.user.create(session, user)) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Account {user.account!r} has been used",
        )
    return created_user


@router.patch("/me", response_model=UserRead)
async def update_me(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(manager),
    *,
    update: UserUpdate,
):
    return await query.user.update(session, user, update)


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(
    session: AsyncSession = Depends(get_session), user: User = Depends(manager)
):
    await query.user.delete(session, user.account)
