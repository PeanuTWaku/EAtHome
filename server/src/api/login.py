from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from .. import auth
from ..database import AsyncSession, get_session

router = APIRouter()


@router.post("/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    username = form.username
    password = form.password

    user = await auth.load_user(username, session)

    is_correct = user and auth.verify_password(password, user.password)

    if not is_correct:
        raise InvalidCredentialsException

    return {"access_token": auth.create_access_token(username)}
