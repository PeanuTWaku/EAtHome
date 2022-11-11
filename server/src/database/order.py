from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .link import OrderProductLink, OrderProductLinkRead
    from .product import ProductRead
    from .shop import Shop
    from .user import User


class OrderStatus(Enum):
    PLACE = "placed"
    FINISH = "finished"
    CANCEL = "canceled"


class OrderMethod(Enum):
    PICKUP = "pickup"
    DELIVERY = "delivery"


class Order(SQLModel, table=True):
    """Represent the fields of an order stored in database."""

    id: int | None = Field(primary_key=True, default=None)
    status: OrderStatus
    created_at: datetime
    finished_at: datetime | None = None
    method: OrderMethod
    subtotal: int = Field(ge=0)
    delivery_fee: int = Field(ge=0)

    customer_account: str = Field(foreign_key="user.account")
    customer: "User" = Relationship(back_populates="orders")

    shopname: str = Field(foreign_key="shop.name")
    shop: "Shop" = Relationship(back_populates="orders")

    product_links: list["OrderProductLink"] = Relationship(back_populates="order")


class OrderRead(SQLModel):
    """Represent the response model for an order."""

    id: int
    status: OrderStatus
    created_at: datetime = Field(alias="createdAt")
    finished_at: datetime | None = Field(alias="finishedAt")
    method: OrderMethod
    subtotal: int
    delivery_fee: int = Field(alias="deliveryFee")

    class Config:
        # allow initialized by field names, but response in aliases
        allow_population_by_field_name = True


class OrderProductRead(OrderRead):
    """Represent the response model for an order and the products in it."""

    products: list["OrderProductLinkRead"]


class OrderCreate(SQLModel):
    """Represent the input fields for creating an order."""

    status: OrderStatus
    created_at: datetime = Field(alias="createdAt")
    method: OrderMethod
    subtotal: int = Field(ge=0)
    delivery_fee: int = Field(ge=0, alias="deliveryFee")


class OrderUpdate(SQLModel):
    """Represent the fields of an order that can be updated through api routes."""

    status: OrderStatus | None = None
    finished_at: datetime | None = Field(default=None, alias="finishedAt")
