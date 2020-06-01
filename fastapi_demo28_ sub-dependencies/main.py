from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: str = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/demo01/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}

# 上述例子存在多重依赖
# FastAPI 将知道它必须首先解决 query_extractor ，然后 query_or_cookie_extractor 在调用它时将结果传递给它。
# GET请求：http://127.0.0.1:8000/demo01/?q=test
# 返回结果：
"""
{
    "q_or_cookie": "test"
}
"""
# 如果后面不加q的参数则返回null,对于Cookie还理解不够
# 如下： http://127.0.0.1:8000/demo01/
"""
{
    "q_or_cookie": null
}
"""

