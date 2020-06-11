from typing import Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []


@app.post("/items/", response_model=Item, summary="Create an item")  # summary 给这个接口做接口的描述
async def create_item(*, item: Item):
    """
    Create an item with all the information:
    # 这个可以描述每个返回字典的表示或者接口功能
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item

"""
意思例子主要是接口的一些说明的显示：

# summary 给这个接口做接口的描述
# 接口函数下的的字段说明
访问url: http://127.0.0.1:8010/docs#/default/create_item_items__post
可以看到上面相应的说明
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8010)
