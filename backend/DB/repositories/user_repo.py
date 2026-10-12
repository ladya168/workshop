from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import UserAddMod, UserGetMod, UserPatchMod
from ..db import Users






class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_user_to_id(self, user_id: int) -> UserGetMod:
        query = select( 
                    Users.username,
                    Users.surname,
                    Users.email,
                    Users.phone_number, 
                    Users.registration_date
                    ).where(Users.id == user_id)
        result = await self.session.execute(query)
        user_mapping = result.mappings().first()
        if not user_mapping:
            return None
        return UserGetMod.model_validate(user_mapping)

    async def add_user(self, user: UserAddMod):
        
        if (await self.session.execute(
            select(Users.id)
            .where(Users.username == user.username,
             Users.surname == user.surname))
             ).scalar_one_or_none():
                    return None

        user_d = user.model_dump()
        
        query = Users(**user_d)
        self.session.add(query)
        await self.session.flush()
        user_id = query.id
        await self.session.commit()
        return user_id

    async def patch_user(self, user_id: int, update_data: UserPatchMod):
        user = await self.session.get(Users, user_id)

        if not user:
            return None

        data_to_update = update_data.model_dump(exclude_unset=True)
        for key, value in data_to_update.items():
            setattr(user, key, value) 

        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, user_id: int):
        user = await self.session.get(Users, user_id)

        if not user:
            return None
            
        await self.session.delete(user)
        await self.session.commit()
        return True