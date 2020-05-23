from typing import List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []  # 嵌套了列表
    values: Set[str] = ()  # 嵌套了集合
    infos: Dict = dict()  # 嵌套了字典
    image: Image = None  # 使用子模型作为类型   觉得和嵌套字典差不多


@app.post("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# 请求：http://127.0.0.1:8000/items/666/
# body:
"""

{
    "name": "zzz",
    "description": "The pretender",
    "price":23.33,
    "tax":15.66,
    "tags":[1,2,3,4],
    "values":["111","2222","34432"],
    "infos":{"name":"hhhh"},
    "image":{"url":"http://127.0.0.1:8000/items/666/","name":"ooo"}
    
}


"""

# 返回结果：
"""
{
    "item_id": 666,
    "item": {
        "name": "zzz",
        "description": "The pretender",
        "price": 23.33,
        "tax": 15.66,
        "tags": [
            "1",
            "2",
            "3",
            "4"
        ],
        "values": [
            "34432",
            "2222",
            "111"
        ],
        "infos": {
            "name": "hhhh"
        },
        "image": {
            "url": "http://127.0.0.1:8000/items/666/",
            "name": "ooo"
        }
    }
}
"""
