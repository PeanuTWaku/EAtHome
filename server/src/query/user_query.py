from typing import Any

from .. import auth
from ..database import AsyncSession
from ..database.user import User, UserCreate, UserUpdate
from .base_query import BaseQuery


class UserQuery(BaseQuery[User, UserCreate, UserUpdate]):
    async def create(self, session: AsyncSession, obj: UserCreate) -> User:
        obj.password = auth.create_password_hash(obj.password)
        return await super().create(session, obj)

    async def update(
        self, session: AsyncSession, db_obj: User, obj: UserUpdate | dict[str, Any]
    ) -> User:
        update_data = obj if isinstance(obj, dict) else obj.dict(exclude_unset=True)

        if (password := update_data.get("password", None)) is not None:
            update_data["password"] = auth.create_password_hash(password)

        return await super().update(session, db_obj, obj)


user = UserQuery(User)
