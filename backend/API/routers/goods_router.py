from fastapi import APIRouter, Depends, HTTPException

from API.repo import get_goods_repo
from DB.models import GoodsGetMod
from DB.repositories.goods_repo import GoodsRepository


router_Goods = APIRouter(prefix="/goods", tags=["Goods"])

@router_Goods.get("/")
async def adadas():
    return "asdasdasds"


@router_Goods.get('/{product_id}', response_model=GoodsGetMod)
async def get_product(
    product_id: int, repo: GoodsRepository = Depends(get_goods_repo)
):
  product = await repo.get_product_with_category(product_id)

  if not product:
    raise HTTPException(status_code=404, detail='Товар не найден')

  return product