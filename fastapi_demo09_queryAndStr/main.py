from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 正常访问如下：http://127.0.0.1:8000/items/?q=eq4   GET
# 返回结果：
"""
{
    "items": [
        {
            "item_id": "Foo"
        },
        {
            "item_id": "Bar"
        }
    ],
    "q": "eq4"
}
"""

# 如果q超过50个字符,返回的结果如下,字符串小于3个字符也会有相应的错误提示：
"""
{
    "detail": [
        {
            "loc": [
                "query",
                "q"
            ],
            "msg": "ensure this value has at most 50 characters",
            "type": "value_error.any_str.max_length",
            "ctx": {
                "limit_value": 50
            }
        }
    ]
}
"""


@app.get("/items_demo01/")  # 没有得到验证
async def read_items_demo01(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/lists/")
async def read_lists(q: List[str] = Query(None)):
# async def read_items(q: List[str] = Query(["hhh", "zzz"])):
    query_items = {"q": q}
    return query_items

# list 如果没有提供值 ，您还可以定义默认值
# 以上为默认值为None
# 可以改为： ["hhh", "zzz"]  只要有输出值，默认值自动失效
# 请求：http://localhost:8000/lists/?q=qqq&q=ssss
# 返回结果：
"""
{
    "q": [
        "qqq",
        "ssss"
    ]
}
"""


@app.get("/alias/")
async def read_alias(q: str = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "ooo"}, {"item_id": "nnn"}]}
    if q:
        results.update({"q": q})
    return results

# 请求： http://127.0.0.1:8000/alias/?item-query=hhh
# 也就是q可以用别名:item-query 来代替
# 返回结果
"""
{
    "items": [
        {
            "item_id": "ooo"
        },
        {
            "item_id": "nnn"
        }
    ],
    "q": "hhh"
}
"""
@app.get("/regex/")
async def read_regex(
    q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
):
    """

    :param q: regex 使得只能为：fixedquery  ，以后可以修改为其他的正则
    :return:
    """
    results = {"items": [{"item_id": "ooo"}, {"item_id": "rrr"}]}
    if q:
        results.update({"q": q})
    return results

# 请求： http://127.0.0.1:8000/regex/?q=fixedquery
# 返回结果：
"""
{
    "items": [
        {
            "item_id": "ooo"
        },
        {
            "item_id": "rrr"
        }
    ],
    "q": "fixedquery"
}
"""
