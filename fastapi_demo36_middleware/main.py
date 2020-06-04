import time

from fastapi import FastAPI, Request, Depends
from fastapi.security import OAuth2PasswordBearer

# from pydantic import BaseModel
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# 使用'X-'前缀 添加自定义专有标 头
"""
浏览器中的客户端能够看到自定义标头，
则需要使用Starlette的CORS文档中记录的 参数 将其添加到CORS配置（ CORS（跨源资源共享） ）
expose_headers中 。

也可以使用 from starlette.requests import Request 。
FastAPI 为开发人员提供了便利。 但它直接来自Starlette。
"""

# 以上的例子暂时还不知道怎么测试其功能

# @app.get("/users/")
# async def read_users(commons: dict = Depends(add_process_time_header)):
#     return commons
