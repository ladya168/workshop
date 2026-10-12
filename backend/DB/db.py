import datetime

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from config import settings

engine = create_async_engine(settings.db_url_sqlite)
Session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    surname: Mapped[str | None]
    email: Mapped[str]
    phone_number: Mapped[str]
    password: Mapped[str]
    registration_date: Mapped[datetime.date]