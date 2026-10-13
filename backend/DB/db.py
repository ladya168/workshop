import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship
from config import settings

engine = create_async_engine(settings.db_url_sqlite)
Session_maker = async_sessionmaker(engine)

async def get_session():
    async with Session_maker() as s:
        yield s



class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    surname: Mapped[str] = mapped_column( default="")
    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str]
    password: Mapped[str]
    registration_date: Mapped[datetime.date] = mapped_column(server_default=func.current_date())

class Goods(Base):
    __tablename__ = "Goods"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    picture: Mapped[str] = mapped_column(default="")
    price: Mapped[float]
    quantity: Mapped[int]
    description: Mapped[str]
    category: Mapped["Categories"] = relationship(back_populates="goods")
    category_id: Mapped[int] = mapped_column(ForeignKey("Categories.id"))

class Categories(Base):
    __tablename__ = 'Categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str]
    goods: Mapped[list["Goods"]] = relationship(
        back_populates="category", 
        cascade= 'all, delete-orphan'
    )


async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)