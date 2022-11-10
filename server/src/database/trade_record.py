from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User


class TradeAction(Enum):
    RECHARGE = "recharge"
    ORDER = "order"
    CANCEL = "cancel"


class TradeRecord(SQLModel, table=True):
    id: int = Field(primary_key=True)
    amount: int = Field(ge=0)
    action: TradeAction
    created_at: datetime
    initiator: str
    recipient: str

    user_account: str = Field(foreign_key="user.account")
    user: "User" = Relationship(back_populates="trade_records")


class TradeRecordRead(SQLModel):
    amount: int
    action: TradeAction
    created_at: datetime
    initiator: str
    recipient: str


class TradeRecordCreate(SQLModel):
    amount: int = Field(ge=0)
    action: TradeAction
    created_at: datetime
    initiator: str
    recipient: str


class TradeRecordUpdate(SQLModel):
    amount: int | None = Field(default=None, ge=0)
    action: TradeAction | None = None
    created_at: datetime | None = None
    initiator: str | None = None
    recipient: str | None = None
