from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models import BaseORM


class UserORM(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
