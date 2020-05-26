from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


# GET请求：http://127.0.0.1:8000/items/?q=dnkden&skip=5&limit=50
# 返回结果：
"""
{
    "q": "dnkden",
    "skip": 5,
    "limit": 50
}
"""

# http://127.0.0.1:8000/users/?q=dnkden&skip=5&limit=50
"""
{
    "q": "dnkden",
    "skip": 5,
    "limit": 50
}
"""
