from fastapi import APIRouter, Depends, HTTPException, status
from API.repo import get_user_repo
from DB.models import UserAddMod, UserPatchMod
from DB.repositories.user_repo import UserRepository

router_Users = APIRouter(prefix="/users", tags=["Users"])


@router_Users.post("/new")
async def add_new_user(user_data: UserAddMod, repo: UserRepository = Depends(get_user_repo)):
    result = await repo.add_user(user_data)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user has been created ago")
    return {"status": "Ok", "user_id": result} 


@router_Users.patch("/{user_id}")
async def patch_user_to_id(user_id: int, update_data: UserPatchMod, repo: UserRepository = Depends(get_user_repo)):
    result= await repo.patch_user(user_id, update_data)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return {"status": "Ok"}


@router_Users.get("/{user_id}")
async def get_user(user_id: int, repo: UserRepository = Depends(get_user_repo)):
    result = await repo.get_user_to_id(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return result

@router_Users.delete("/{user_id}")
async def delete_user(user_id:int, repo: UserRepository = Depends(get_user_repo)):
    result = await repo.delete_user(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return {"status": "Ok"}

