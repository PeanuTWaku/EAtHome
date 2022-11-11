from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderProductLink(SQLModel, table=True):
    order_id: int = Field(foreign_key="order.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    quantity: int

    order: "Order" = Relationship(back_populates="product_links")
    product: "Product" = Relationship(back_populates="order_links")


class OrderProductLinkRead(SQLModel):
    product: Product
    quantity: int


class OrderProductLinkCreate(SQLModel):
    order_id: int = Field(foreign_key="order.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)
    quantity: int
