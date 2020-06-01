from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items_01/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users_01/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# demo01 返回字典的依赖项
# https://www.pythonf.cn/read/56918
# GET请求访问： http://127.0.0.1:8000/items_01/?q=one&skip=5&limit=15
# 返回结果：
"""
{
    "q": "one",
    "skip": 5,
    "limit": 15
}
"""

# get请求访问：http://127.0.0.1:8000/users_01/?q=one&skip=5&limit=15
# 返回结果：
"""
{
    "q": "one",
    "skip": 5,
    "limit": 15
}
"""

"""
对上面两个例子的理解是：请求路由不同，但是请求的效果返回值是一样的
"""


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items_02/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    """
    需要记住这样的使用:
    CommonQueryParams两次出现
    :param commons:
    :return:
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

# 以上的例子是将改为类的实例化变量返回

# GET请求： http://127.0.0.1:8000/items_02/?q=one&skip=1&limit=15
# 返回结果：返回的是在items从起始skip到limit中间的数据
"""
{
    "q": "one",
    "items": [
        {
            "item_name": "Bar"
        },
        {
            "item_name": "Baz"
        }
    ]
}
"""


