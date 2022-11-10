from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .order import Order
    from .shop import Shop


class UserRead(SQLModel):
    """Represent the response model for a user."""

    account: str
    display_name: str = Field(alias="displayName")
    phone: str
    latitude: float
    longitude: float
    balance: int

    shopname: str | None


class UserCreate(SQLModel):
    """Represent the input fields for creating a user."""

    account: str = Field(regex=r"\w+")
    password: str
    display_name: str = Field(alias="displayName")
    phone: str = Field(regex=r"09\d{8}")
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class User(SQLModel, table=True):
    """Represent the fields of a user stored in database."""

    account: str = Field(regex=r"\w+", primary_key=True)
    password: str
    display_name: str
    phone: str = Field(regex=r"09\d{8}")
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    balance: int = Field(default=0, ge=0)

    shopname: str | None = Field(None, foreign_key="shop.name")
    shop: "Shop" | None = Relationship(back_populates="owner")

    order_ids: list[int] = Field(None, foreign_key="order.id")
    orders: list["Order"] = Relationship(back_populates="customer")


class UserUpdate(SQLModel):
    """Represent the fields of a user that can be updated through api routes."""

    password: str | None = None
    display_name: str | None = None
    phone: str | None = Field(default=None, regex=r"09\d{8}")
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)
