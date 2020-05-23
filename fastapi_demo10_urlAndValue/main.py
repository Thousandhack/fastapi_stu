from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),  # 这个path不知道干什么的
        q: str = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    print(q)
    if q:
        results.update({"q": q})
    return results


# 请求： http://localhost:8000/items/5/?item-query=qqqqvalue  使用的别名，使用的q参数是不行的
# 返回结果：
"""
{
    "item_id": 5,
    "q": "qqqqvalue"
}
"""


@app.get("/demo01/{demo_id}/")
async def read_demo01(
        *,
        demo_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000),  # 大于和小于或等于
        q: str,
):
    results = {"demo_id": demo_id}
    if q:
        results.update({"q": q})
    return results


# 请求： http://localhost:8000/demo01/577/?q=ewqeq
# demo_id 不能超过1000 不小于 1
# 返回结果：
"""
{
    "demo_id": 577,
    "q": "ewqeq"
}
"""


@app.get("/demo02/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),  # 取值范围 [0,1000]
        q: str,
        size: float = Query(..., gt=0, lt=10.5)  # 不大于 10.5 不小于0 ，而且0.0不符合
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results


# 请求： http://localhost:8000/demo02/577/?q=ewq&size=1.6
# 返回结果：
"""
{
    "item_id": 577,
    "q": "ewq",
    "size": 1.6
}
"""


