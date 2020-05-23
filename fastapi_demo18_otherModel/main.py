# 多种型号
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str = None


def fake_password_hasher(raw_password: str):
    """
    主要功能是给密码加盐
    :param raw_password:
    :return:
    """
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    """
    主要功能保存用户信息
    :param user_in:
    :return:
    """
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(*, user_in: UserIn):
    """
    创建用户，返回用户信息，不包括密码
    :param user_in:
    :return:
    """
    user_saved = fake_save_user(user_in)
    return user_saved


# 请求： http://127.0.0.1:8000/user/    POST
# body:
"""
{
    "username": "john",
    "password": "wqeqeq",
    "email": "john.doe@example.com",
    "full_name": None,
}
"""

# 返回结果：
"""
{
    "username": "john",
    "email": "john.doe@example.com",
    "full_name": ""
}
"""


# 减少重复
class UserBase1(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserIn1(UserBase1):
    password: str


class UserOut1(UserBase1):
    pass


class UserInDB1(UserBase1):
    hashed_password: str


def fake_password_hasher1(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user1(user_in: UserIn1):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB1(**user_in.dict(), hashed_password=hashed_password)
    print("User1 saved! ..not really")
    return user_in_db


@app.post("/user1/", response_model=UserOut1)
async def create_user(*, user_in: UserIn1):
    user_saved = fake_save_user(user_in)
    return user_saved


# 请求：http://127.0.0.1:8000/user1/
# Body:
"""
{
    "username": "one",
    "password": "wqeqeq",
    "email": "one.doe@example.com",
    "full_name": "one_one"
}
"""
# 返回结果：
"""
{
    "username": "one",
    "email": "one.doe@example.com",
    "full_name": "one_one"
}
"""


# Union 或 anyOf
# Union 里面可以放入多个模型

class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


base_items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/base_items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_base_item(item_id: str):
    return base_items[item_id]


# 请求： http://127.0.0.1:8000/base_items/item2/    GET

# 返回结果：
"""
{
    "description": "Music is my aeroplane, it's my aeroplane",
    "type": "plane",
    "size": 5
}
"""

# 也可以使用模型清单
from typing import List


class Listmode(BaseModel):
    name: str
    description: str


@app.get("/lists/", response_model=List[Listmode])  # 返回列表的json的格式数据
async def read_list():
    items_list = [
        {"name": "Foo", "description": "There comes my hero"},
        {"name": "Red", "description": "It's my aeroplane"},
    ]
    return items_list


# 请求： http://127.0.0.1:8000/lists/    GET
# 返回结果：
"""
[
    {
        "name": "Foo",
        "description": "There comes my hero"
    },
    {
        "name": "Red",
        "description": "It's my aeroplane"
    }
]
"""

# 任意响应 dict  （重要重要，估计以后会常用）

from typing import Dict


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


# GET请求：  http://127.0.0.1:8000/keyword-weights/
# 返回结果：
"""
{
    "foo": 2.3,
    "bar": 3.4
}
"""

# 按以下教程学习的demo
# https://www.pythonf.cn/read/56907
