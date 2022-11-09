from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .shop import Shop


class UserRead(SQLModel):
    """Represent the response model for a user."""

    account: str
    display_name: str
    phone: str
    latitude: float
    longitude: float
    balance: int

    shopname: Optional[str]


class UserCreate(SQLModel):
    """Represent the input fields for creating a user."""

    account: str = Field(regex=r"\w+")
    password: str
    display_name: str
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

    shopname: Optional[str] = Field(None, foreign_key="shop.name")
    shop: Optional[Shop] = Relationship(back_populates="owner")


class UserUpdate(SQLModel):
    """Represent the fields of a user that can be updated through api routes."""

    password: Optional[str] = None
    display_name: Optional[str] = None
    phone: Optional[str] = Field(default=None, regex=r"09\d{8}")
    latitude: Optional[float] = Field(default=None, ge=-90, le=90)
    longitude: Optional[float] = Field(default=None, ge=-180, le=180)
