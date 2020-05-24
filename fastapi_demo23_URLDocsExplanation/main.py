from typing import Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []


@app.post("/demo01/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(*, item: Item):
    return item


# POST请求： http://127.0.0.1:8000/demo01/
# body数据：
"""
{
	"name":"2222",
	"price":332.22,
	"tags":["12","wee"]
}
"""

# 返回结果:
"""
{
    "name": "2222",
    "description": null,
    "price": 332.22,
    "tax": null,
    "tags": [
        "wee",
        "12"
    ]
}
"""


@app.post("/demo02/", response_model=Item, tags=["items"])
async def create_item(*, item: Item):
    return item


# tags 类似一个url里面的分类，在docs里面可以提现 相应的接口文档再在items的类别下


# 摘要和描述
# 添加 summary 和 description
@app.post(
    "/demo03/",
    response_model=Item,
    summary="这个是一个创建ITEM的接口",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags"
                "创建的具体描述",
)
async def create_item(*, item: Item):
    return item


# 在docs 的API文档中 url 后面有有一个描述 接口的大概摘要
# 点击进去有具体的接口文档的描述：这些都是可以自己定义的


@app.post("/demo04/", response_model=Item, summary="Create an item")
async def create_item(*, item: Item):
    """
    这个发送请求的字段参数说明
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# 相应说明
# 使用参数指定响应描述 response_description
@app.post(
    "/demo05/",
    response_model=Item,
    summary="Create an item 05",
    response_description="The created item 05",
)
async def create_item(*, item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# 弃用一个 路径操作
# 已弃用 ，但不删除它，则传递参数 deprecated 
# 在交互式文档中，它将被明确标记为不推荐使用
@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
