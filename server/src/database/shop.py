from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .order import Order
    from .product import Product
    from .user import User


class Shop(SQLModel, table=True):
    """Represent the fields of a shop stored in database."""

    name: str = Field(primary_key=True)
    category: str = Field(index=True)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    revenue: int = Field(default=0, ge=0)

    owner_name: str = Field(foreign_key="user.account")
    owner: "User" = Relationship(back_populates="shop")

    orders: list["Order"] = Relationship(back_populates="shop")
    products: list["Product"] = Relationship(back_populates="shop")


class ShopRead(SQLModel):
    """Represent the response model for a shop."""

    name: str
    category: str
    latitude: float
    longitude: float
    revenue: int

    owner_name: str = Field(alias="ownerName")

    class Config:
        # allow initialized by field names, but response in aliases
        allow_population_by_field_name = True


class ShopCreate(SQLModel):
    """Represent the input fields for creating a shop."""

    name: str
    category: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

    owner_name: str = Field(alias="ownerName")


class ShopUpdate(SQLModel):
    """Represent the fields of a shop that can be updated through api routes."""

    category: str | None = None
    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)
