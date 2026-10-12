from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from db import Base, Session, Users


async def get_user_to_id(id: int, session: AsyncSession = Session(), db: Base = Users ):
    query = select(db.username, db.surname, db.email, db.phone_number, db.registration_date).where(db.id == id)
    async with session() as s:
        pass
