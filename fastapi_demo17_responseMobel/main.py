from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []


@app.post("/demo01/", response_model=Item)
async def create_item(item: Item):
    return item


# 请求： http://127.0.0.1:8000/demo01/

# body请求体内容：
"""
{
	"name":"hsz",
	"descroption":"test my hhh",
	"price":11.22,
	"tax":1123.22,
	"tags":["zero","one"]
}
"""
# 返回结果：
"""
{
    "name": "hsz",
    "description": null,
    "price": 11.22,
    "tax": 1123.22,
    "tags": [
        "zero",
        "one"
    ]
}
"""


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr  # 格式为 字符串+@
    full_name: str = None


# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(*, user: UserIn):
    return user


# 请求：http://127.0.0.1:8000/user/
# body :
"""
{
	"username":"hhh",
	"password":"ddweew",
	"email":"123@qq.com",
	"full_name":"dwqqdqdq"
}
"""
# 返回结果：
"""
{
    "username": "hhh",
    "password": "ddweew",
    "email": "123@qq.com",
    "full_name": "dwqqdqdq"
}
"""


class Demo03(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


demo03 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/demo03/{demo03_id}", response_model=Demo03,
         response_model_exclude_unset=True)  # response_model_exclude_unset=True 表示返回数据不包含默认值
async def read_item(demo03_id: str):
    return demo03[demo03_id]


# 请求：  http://127.0.0.1:8000/demo03/foo  GET方法
# 返回结果：
"""
{
    "name": "Foo",
    "price": 50.2
}
"""


class Demo04(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5


demo04 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "one", "description": "The one fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/demo04/{demo04_id}/name",
    response_model=Demo04,
    response_model_include={"name", "description"},  # 表示返回的body的键值对的键包括这两个键
)
async def read_demo04_name(demo04_id: str):
    return demo04[demo04_id]


# 请求：http://127.0.0.1:8000/demo04/foo/name
# 返回结果：
"""
{
    "name": "Foo",
    "description": null
}
"""


@app.get(
    "/demo04/{demo04_id}/public",
    response_model=Demo04,
    response_model_exclude={"tax"})  # 表示返回不包括tax的键
async def read_item_public_data(demo04_id: str):
    return demo04[demo04_id]

# 请求：http://127.0.0.1:8000/demo04/bar/public
# 返回结果：
"""
{
    "name": "one",
    "description": "The one fighters",
    "price": 62.0
}
"""


