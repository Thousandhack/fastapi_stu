from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


# 1.单个body的情况
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.put("/demo01/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str = None,
        item: Item = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# 请求： http://localhost:8000/demo01/1000/?q=ewq&size=1.6
# body的内容为：
"""
{
    "name": "hsz",
    "description": "a coder",
    "price": 452.2,
    "tax": 322.5
}
"""

# 返回结果：
"""
{
    "item_id": 1000,
    "q": "ewq",
    "item": {
        "name": "hsz",
        "description": "a coder",
        "price": 452.2,
        "tax": 322.5
    }
}
"""


# 2.多个body的情况


class Teacher(BaseModel):
    name: str
    age: int


class User(BaseModel):
    username: str
    full_name: str = None


@app.put("/demo02/{user_id}")
async def update_demo02(*, user_id: int, teacher: Teacher, user: User):
    results = {"user_id": user_id, "teacher": teacher, "user": user}
    return results


# 请求： http://localhost:8000/demo02/666/
# body 数据：
"""
{
    "teacher": {
        "name": "Foo",
        "age": 25
    },
    "user": {
        "username": "hu",
        "full_name": "hu ge"
    }
}
"""
# 返回：
"""
{
    "user_id": 666,
    "teacher": {
        "name": "Foo",
        "age": 25
    },
    "user": {
        "username": "hu",
        "full_name": "hu ge"
    }
}
"""

# 3.体内的奇异值 今天到这啦
from fastapi import Body


class T1(BaseModel):
    name: str
    age: int


class T2(BaseModel):
    username: str


@app.put("/demo03/{id}")
async def update_demo03(*, id: int, t1: T1, t2: T2, importance: int = Body(...)):
    results = {"user_id": id, "t1": t1, "t2": t2, "importance": importance}
    return results


# 请求： http://127.0.0.1:8000/demo03/666/   PUT方法
# body 数据
"""
{
    "t1": {
        "name": "Foo",
        "age": 25
    },
    "t2": {
        "username": "hu"
    },
    "importance": 5
}
"""
# 返回结果：
"""
{
    "user_id": 666,
    "t1": {
        "name": "Foo",
        "age": 25
    },
    "t2": {
        "username": "hu"
    },
    "importance": 5
}
"""


# 4.嵌入单机身参数

class T5(BaseModel):
    name: str
    description: str = None


@app.put("/demo05/{item_id}")
async def update_demo05(*, item_id: int, t5: T5 = Body(..., embed=True)):
    results = {"item_id": item_id, "item": t5}
    return results


# 请求： http://127.0.0.1:8000/demo05/666/
# body:
"""
{
    "t5": {
        "name": "zzz",
        "description": "The coder"
    }
}
"""
# 代替：原本应该输入
"""
{
    "name": "zzz",
    "description": "The coder"
}
"""
# 返回结果：
"""
{
    "item_id": 666,
    "item": {
        "name": "zzz",
        "description": "The coder"
    }
}
"""
