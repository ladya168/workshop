from fastapi import APIRouter, HTTPException

from API.repo import GoodsRepoSchema
from DB.models import GoodsGetMiniMod, GoodsGetMod, GoodsMod



router_Goods = APIRouter(prefix="/goods", tags=["Goods"])

@router_Goods.get("/all", response_model=list[GoodsGetMiniMod])
async def get_all_mini(repo: GoodsRepoSchema):
    result = await repo.get_all_products_mini()

    if not result:
       raise HTTPException

    return result


@router_Goods.get('/{product_id}', response_model=GoodsGetMod)
async def get_product(product_id: int, repo: GoodsRepoSchema):
    result = await repo.get_product_to_id(product_id)

    if not result:
      raise HTTPException(status_code=404, detail='Товар не найден')

    return result

@router_Goods.post("/new")
async def add_product(product:GoodsMod ,repo: GoodsRepoSchema):
   
   result = await repo.add_product(product)

   if not result:
      raise HTTPException(status_code=500, detail='asdasdasds')

   return {"status": "Ok", "Product_id": result}