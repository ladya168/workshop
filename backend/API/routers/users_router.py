from fastapi import APIRouter, HTTPException, Response, status
from API.repo import UserRepoSchema
from DB.models import UserAddMod, UserPatchMod

from JWT.auth import auth_user, create_token
from JWT.schemas import IdSchema

router_Users = APIRouter(prefix="/users", tags=["Users"])
 

@router_Users.post("/new")
async def reg_user(user_data: UserAddMod, response: Response, repo: UserRepoSchema ):
    result = await repo.add_user(user_data)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user has been created ago")
    token_id = await create_token(result)
    token_role = await auth_user(user_data)
    response.set_cookie("token_id", token_id)

    response.set_cookie("token_role", token_role)

    return {"status": "Ok", "user_id": result} 

@router_Users.post("/login")
async def log_user(user_data: UserAddMod, response: Response, repo: UserRepoSchema):
    pass


@router_Users.patch("/")
async def patch_user_to_id(user_id: IdSchema, update_data: UserPatchMod , repo: UserRepoSchema):

    result= await repo.patch_user(user_id, update_data)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return {"status": "Ok"}


@router_Users.get("/")
async def get_user(user_id: IdSchema, repo: UserRepoSchema):
    result = await repo.get_user_to_id(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return result

@router_Users.delete("/")
async def delete_user(user_id: IdSchema, repo: UserRepoSchema):
    result = await repo.delete_user(user_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return {"status": "Ok"}

