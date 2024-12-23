from sqlalchemy import BigInteger, String, SmallInteger, DATETIME, Index
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy.sql import func
from enums import UserType
from sql_type import IntEnum


class _Base(DeclarativeBase):
    pass


class User(_Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(256), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(64), nullable=False)
    type: Mapped[UserType] = mapped_column(IntEnum(UserType), nullable=False)
    status: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    first_name: Mapped[str] = mapped_column(String(256), nullable=False)
    last_name: Mapped[str] = mapped_column(String(256), nullable=False)
    age: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    updated_by: Mapped[str] = mapped_column(String(256), nullable=False)
    updated_at: Mapped[str] = mapped_column(DATETIME, nullable=False, server_default=func.now(), onupdate=func.now())
    created_by: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False, server_default=func.now())

    __table_args__ = (Index("index01", "name"),)
