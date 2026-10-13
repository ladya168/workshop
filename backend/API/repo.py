from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from DB.db import get_session
from DB.repositories.category_repo import CategoryRepository
from DB.repositories.goods_repo import GoodsRepository
from DB.repositories.user_repo import UserRepository


def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)

def get_goods_repo(session: AsyncSession = Depends(get_session)) -> GoodsRepository:
    return GoodsRepository(session)

def get_categories_repo(session: AsyncSession = Depends(get_session)) -> CategoryRepository:
    return CategoryRepository(session)

UserRepoSchema = Annotated[UserRepository, Depends(get_user_repo)]

GoodsRepoSchema = Annotated[GoodsRepository, Depends(get_goods_repo)]

CategoriesRepoSchema = Annotated[CategoryRepository, Depends(get_categories_repo)]