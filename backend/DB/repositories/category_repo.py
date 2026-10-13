from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from DB.db import Categories
from ..models import  CategoryInGoodsResponse, CategoryMod


class CategoryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_category(self, category: CategoryMod):
        if (await self.session.execute(
            select(Categories.id)
            .where(Categories.category_name == category.category_name))
             ).scalar_one_or_none():
                    return None

        category_d = category.model_dump()
        query = Categories(**category_d)
        self.session.add(query)
        await self.session.flush()
        category_id = query.id
        await self.session.commit()

        return category_id

    async def get_all_categories(self):
        query = select(Categories)
        result = await self.session.execute(query)
        db_categories = result.scalars().all()

        return [
        CategoryInGoodsResponse.model_validate(categories)
        for categories in db_categories
    ]
    
        
