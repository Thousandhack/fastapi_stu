from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    默认返回10个列表中的数据
    :param skip: 列表起始值
    :param limit: 列表取值数量
    :return: 返回列表结果
    """
    return fake_items_db[skip: skip + limit]


# 访问： http://127.0.0.1:8000/items/?skip=1&limit=1
# 返回：
# [
#     {
#         "item_name": "Bar"
#     }
# ]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 访问：http://127.0.0.1:8000/items/5/
# 返回：
# {
#     "item_id": "5"
# }
