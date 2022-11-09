from sqlmodel import Field, SQLModel


class UserRead(SQLModel):
    account: str = Field(regex=r"\w+", primary_key=True)
    display_name: str
    phone: str = Field(regex=r"09\d{8}")
    balance: int = Field(0, ge=0)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class UserCreate(UserRead):
    password: str


class User(UserRead, table=True):
    password: str


class UserUpdate(SQLModel):
    password: str | None = None
    display_name: str | None = None
    phone: str | None = Field(None, regex=r"09\d{8}")
    balance: int | None = Field(None, 0, ge=0)
    latitude: float | None = Field(None, ge=-90, le=90)
    longitude: float | None = Field(None, ge=-180, le=180)
