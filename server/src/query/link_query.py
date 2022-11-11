from ..database.link import OrderProductLink, OrderProductLinkCreate
from .base_query import BaseQuery


class OrderProductLinkQuery(BaseQuery[OrderProductLink, OrderProductLinkCreate, None]):
    ...


order_product_link = OrderProductLinkQuery(OrderProductLink)
