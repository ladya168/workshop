from datetime import datetime, timezone, timedelta
from DB.models import UserAddMod
from config import settings
from fastapi import Cookie, HTTPException, status
import jwt





async def get_current_data(token_id: str | None = Cookie(None)):
    if not token_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Не найден токен авторизации в cookies",
        )
    
    try:
        payload = jwt.decode(token_id, settings.secret_key, algorithms=[settings.algorithm])
        
        sub: str | None = payload.get("sub")
        print(1)
        
        if sub is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Некорректный токен",
            )
        return sub
        
    except jwt.PyJWTError:
        print(2)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Недействительный токен",
        )

async def get_id():
    return int(await get_current_data())


async def create_token(data: str):
    payload ={
        "sub": data,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)



Admin = UserAddMod(username=settings.admin_name,
                   surname=settings.admin_surname,
                   email=settings.admin_email,
                   phone_number=settings.admin_phonenum,
                   password=settings.admin_pass)



async def auth_user(user: UserAddMod):
    print(user.model_dump())
    print(Admin.model_dump())
    if (user.username == Admin.username
        and
        user.email == Admin.email
        and
        user.surname == Admin.surname
        and
        user.phone_number == Admin.phone_number
        and
        user.password == Admin.password):
        print("sdadsas")
        return await create_token("admin") 
    else:
        print("abob")
        return await create_token("user")




