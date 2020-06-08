# 为了避免SQLAlchemy 模型 和Pydantic 模型 之间的混淆
# 使用 models.py 带有SQLAlchemy模型的文件，以及 schemas.py 带有Pydantic模型 的文件
from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
