from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base_model import BaseModel


class Referrals(BaseModel):
    __tablename__ = 'referrals'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True, autoincrement=True,
        unique=True, nullable=False,
    )
    referral: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False
    )

    inviter: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False
    )
