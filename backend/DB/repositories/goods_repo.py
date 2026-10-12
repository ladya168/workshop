from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from ..models import  GoodsGetMiniMod, GoodsGetMod, GoodsMod
from ..db import Goods 

class GoodsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_product(self, product: GoodsMod):
        product_d = product.model_dump()
        query = Goods(**product_d)

        self.session.add(query)

        await self.session.commit()

        await self.session.refresh(query)
        if not query.id:
            return None

        return query.id

    async def get_all_products_mini(self):
        query = select(Goods.id,
                       Goods.product_name,
                       Goods.picture,
                       Goods.price_in_rubles, 
                       Goods.category).options(joinedload(Goods.category))
        result = self.session.execute(query)
        db_products = result.scalars().all()

        return [
        GoodsGetMiniMod.model_validate(product)
        for product in db_products
    ]

    async def get_product_to_id(self, product_id: int):
        query = select(
            Goods
        ).options(joinedload(Goods.category)).where(Goods.id == product_id)

        result = self.session.execute(query)
        db_product = result.scalar_one_or_none()

        if not db_product:
            return None

        return GoodsGetMod.model_validate(db_product)

