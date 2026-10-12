from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from DB.db import get_session
from DB.repositories.goods_repo import GoodsRepository
from DB.repositories.user_repo import UserRepository


def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)

def get_goods_repo(session: AsyncSession = Depends(get_session)) -> GoodsRepository:
    return GoodsRepository(session)