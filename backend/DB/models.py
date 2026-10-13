import datetime
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

class UserMod(BaseModel):
    username: str
    surname: str | None
    email: EmailStr
    phone_number: PhoneNumber
    password: str
    registration_date: datetime.date

    model_config = ConfigDict(from_attributes=True)

class UserGetMod(BaseModel):
    username: str
    surname: str | None
    email: EmailStr
    phone_number: PhoneNumber
    registration_date: datetime.date

    model_config = ConfigDict(from_attributes=True)

class UserAuthMod(BaseModel):
    username: str
    surname: str | None
    email: EmailStr
    phone_number: PhoneNumber

    model_config = ConfigDict(from_attributes=True)



class UserAddMod(BaseModel):
    username: str
    surname: str | None
    email: EmailStr
    phone_number: PhoneNumber
    password: str

    model_config = ConfigDict(from_attributes=True)



class UserPatchMod(BaseModel):
    username: str | None = None
    surname: str | None = None
    email: EmailStr | None = None
    phone_number: PhoneNumber | None = None
    password: str | None = None


class CategoryMod(BaseModel):
    category_name: str

    model_config = ConfigDict(from_attributes=True)

class GoodsMod(BaseModel):
    product_name: str
    picture: str
    price: float
    quantity: int = 1
    description: str
    category_id: int



class CategoryInGoodsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_name: str



class GoodsGetMod(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_name: str
    picture: str
    price: float
    quantity: int = 1
    description: str
    category: CategoryInGoodsResponse


class GoodsGetMiniMod(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_name: str
    picture: str
    price: float
    category: CategoryInGoodsResponse

