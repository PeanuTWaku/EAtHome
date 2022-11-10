from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .link import OrderProductLink
    from .shop import Shop


class Product(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    image_url: str
    price: int = Field(ge=0)
    quantity: int = Field(ge=0)

    order_links: list["OrderProductLink"] = Relationship(back_populates="product")

    shopname: str = Field(foreign_key="shop.name")
    shop: "Shop" = Relationship(back_populates="products")


class ProductRead(SQLModel):
    name: str
    image_url: str
    price: int
    quantity: int


class ProductCreate(SQLModel):
    name: str
    image_url: str
    price: int = Field(ge=0)
    quantity: int = Field(ge=0)


class ProductUpdate(SQLModel):
    name: str | None = None
    image_url: str | None = None
    price: int | None = Field(default=None, ge=0)
    quantity: int | None = Field(default=None, ge=0)
