from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base_model import BaseModel


class History(BaseModel):
    __tablename__ = 'history_questions'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True, autoincrement=True,
        unique=True, nullable=False,
    )
    question: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    type: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    answer: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    answer_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
