from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


# 请求： http://127.0.0.1:8000/items/     POST
# body
"""
{
    "name": "hsz",
    "description": "a coder",
    "price": 452.2,
    "tax": 322.5
}
"""

# 返回：
"""
{
    "name": "hsz",
    "description": "a coder",
    "price": 452.2,
    "tax": 322.5
}
"""

# body 2:
"""
{
    "name": "zero",
    "price": 333.2
}
"""
# 返回：
"""
{
    "name": "zero",
    "description": null,
    "price": 333.2,
    "tax": null
}
"""


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 请求：
# body: http://127.0.0.1:8000/items/5/   方法：PUT
"""
{
    "name": "zero",
    "price": 333.2
}
"""

# 返回：

"""
{
    "item_id": 5,
    "name": "zero",
    "description": null,
    "price": 333.2,
    "tax": null
}
"""
