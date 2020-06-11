from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(item_id: str, name: str = Body(None), size: int = Body(None)):
    if item_id in items:
        item = items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)


# 上面的例子测试：
# PUT请求： http://127.0.0.1:8000/items/hsz/
# 其中hsz一定 不在 items里面的key才能返回201的状态码
# body 数据：
"""
{
	"name":"four@qq.com",
	"size":100
}
"""
# 返回结果：状态码 201
"""
{
    "name": "four@qq.com",
    "size": 100
}
"""
