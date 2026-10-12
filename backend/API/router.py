from fastapi import APIRouter, Depends, HTTPException, status
from API.repo import get_user_repo
from DB.db_requests import UserRepository


router = APIRouter()

@router.get("/{user_id}")
async def get_all_data(user_id: int, repo: UserRepository = Depends(get_user_repo)):
    result = await repo.get_user_to_id(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    pass