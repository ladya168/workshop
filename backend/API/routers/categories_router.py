from fastapi import APIRouter, HTTPException, status

from API.repo import CategoriesRepoSchema

from DB.models import CategoryMod




router_Categories = APIRouter(prefix="/categories", tags=["Categories"])

@router_Categories.post("/new")
async def add_category(category: CategoryMod, repo: CategoriesRepoSchema):
    result = await repo.add_category(category)
    if not result:
        raise HTTPException

    return {"Status": "Ok", "category_id" : result}

@router_Categories.get("/all")
async def all_category(repo: CategoriesRepoSchema):
    result = await repo.get_all_categories()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="dsaasdfsdaf")

    return result

