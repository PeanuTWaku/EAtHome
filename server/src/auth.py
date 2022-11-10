from typing import AsyncIterator

from fastapi_login import LoginManager
from passlib.context import CryptContext

from . import query
from .database import AsyncSession, User, get_session
from .settings import settings

manager = LoginManager(secret=settings.SECRET_KEY, token_url=settings.TOKEN_URL)
context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str):
    return context.hash(password)


def verify_password(password: str, hashed_password: str):
    return context.verify(password, hashed_password)


@manager.user_loader(generate_session=get_session)
async def load_user(
    username: str, generate_session: AsyncIterator[AsyncSession]
) -> User | None:
    async for session in generate_session():
        return await query.user.get_by_id(session, username)


def create_access_token(username: str):
    return manager.create_access_token(data=dict(sub=username))
