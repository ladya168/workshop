from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from DB.db import get_session
from DB.db_requests import UserRepository

def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)

def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return UserRepository(session)