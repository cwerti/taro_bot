from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import ForeignKey, Integer, String, JSON
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from api.app.database.models.base_model import BaseModel
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
)


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True, autoincrement=True,
        unique=True, nullable=False,
    )
    username: Mapped[str] = mapped_column(
        String(32),
        nullable=False, unique=True
    )

    balance: Mapped[str] = mapped_column(
        String, nullable=False,
    )


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], BaseModel):
    __tablename__ = 'access_tokens'

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer,
            ForeignKey("users.id", ondelete="cascade"),
            nullable=False
        )
