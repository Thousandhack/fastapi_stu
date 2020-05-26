from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/demo01/{item_id}", response_model=Item)
async def read_demo01(item_id: str):
    return items[item_id]


# GET请求：http://127.0.0.1:8000/demo01/bar

# 返回结果：
"""
{
    "name": "Bar",
    "description": "The bartenders",
    "price": 62.0,
    "tax": 20.2,
    "tags": []
}
"""


@app.put("/demo01/{item_id}", response_model=Item)
async def update_demo01(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    print(items)
    items[item_id] = update_item_encoded
    print(items)
    return items[item_id]  # 返回更新后的数据


# PUT请求：http://127.0.0.1:8000/demo01/bar
# body 数据为：
"""
{
	"name": "Bar", 
	"description": "The demo01", 
	"price": 79, 
	"tax": 55.2,
	"tags":["one","two"]
	
}
"""

# 返回结果：有个小问题就是不知道为什么不能返回所有数据，或者任意数据,可能是因为限定了返回Model的类型
"""
{
    "name": "Bar",
    "description": "The demo01",
    "price": 79.0,
    "tax": 55.2,
    "tags": [
        "one",
        "two"
    ]
}
"""


@app.patch("/demo02/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


# 使用 HTTP PATCH 操作来 部分 更新数据

# PATCH 请求：http://127.0.0.1:8000/demo02/baz
# body数据：
"""
{
	"name": "baz", 
	"description": "The demo02", 
	"price": 66, 
	"tax": 55.2,
	"tags":["one","three"]
	
}
"""

# 返回结果:
"""
{
    "name": "baz",
    "description": "The demo02",
    "price": 66.0,
    "tax": 55.2,
    "tags": [
        "one",
        "three"
    ]
}
"""
