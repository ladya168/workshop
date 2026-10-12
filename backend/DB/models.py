import datetime
from pydantic import BaseModel

class UserMod(BaseModel):
    username: str
    surname: str | None
    email: str
    phone_number: str
    password: str
    registration_date: datetime.date

    class Config:
        from_attributes = True


class UserUpdateMod(BaseModel):
    username: str | None = None
    surname: str | None = None
    email: str | None = None
    phone_number: str | None = None
    password: str | None = None


class CategoryMod(BaseModel):
    category_name: str


    class Config:
        from_attributes = True