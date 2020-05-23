from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = Field(None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float = None


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

"""
我的理解是Fields的效果是 如果body的数据有错误会提示
"""
# 如下例子：
# 请求：http://127.0.0.1:8000/items/666/
# body:
"""
{
    "item": {
        "name": "zzz",
        "description": "The pretender",
        "price":-23.33
    }
}
"""
# 返回结果：
"""
{
    "detail": [
        {
            "loc": [
                "body",
                "item",
                "price"
            ],
            "msg": "ensure this value is greater than 0",  # 这一句就是表示不能小于0
            "type": "value_error.number.not_gt",
            "ctx": {
                "limit_value": 0
            }
        }
    ]
}
"""


# 以下为正确提交的例子：
# 请求： http://127.0.0.1:8000/items/666/
# body
"""
{
    "item": {
        "name": "zzz",
        "description": "The pretender",
        "price":23.33
    }
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
        "tax": null
    }
}
"""
