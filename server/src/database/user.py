from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .order import Order
    from .shop import Shop


class User(SQLModel, table=True):
    """Represent the fields of a user stored in database."""

    account: str = Field(regex=r"\w+", primary_key=True)
    password: str
    display_name: str
    phone: str = Field(regex=r"09\d{8}")
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    balance: int = Field(default=0, ge=0)

    shop: Optional["Shop"] = Relationship(back_populates="owner")

    orders: list["Order"] = Relationship(back_populates="customer")


class UserRead(SQLModel):
    """Represent the response model for a user."""

    account: str
    display_name: str = Field(alias="displayName")
    phone: str
    latitude: float
    longitude: float
    balance: int

    class Config:
        # allow initialized by field names, but response in aliases
        allow_population_by_field_name = True


class UserCreate(SQLModel):
    """Represent the input fields for creating a user."""

    account: str = Field(regex=r"\w+")
    password: str
    display_name: str = Field(alias="displayName")
    phone: str = Field(regex=r"09\d{8}")
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class UserUpdate(SQLModel):
    """Represent the fields of a user that can be updated through api routes."""

    password: str | None = None
    display_name: str | None = Field(default=None, alias="displayName")
    phone: str | None = Field(default=None, regex=r"09\d{8}")
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)
