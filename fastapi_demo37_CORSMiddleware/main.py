from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware  # 效果同上

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:8000",
    "http://localhost",
]  # 允许进行跨域请求的来源列表

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # 表示跨域请求应支持cookie
    allow_methods=["*"],  # 跨域请求应允许的HTTP方法列表
    allow_headers=["*"],  # 跨域请求应支持的HTTP请求标头列表
)
"""
支持以下参数：

allow_origins -应该允许进行跨域请求的来源列表。 例如 ['https://example.org', 'https://www.example.org'] 。 您可以 ['*'] 用来允许任何来源。
allow_origin_regex -一个正则表达式字符串，与应允许进行跨域请求的原点匹配。 例如。 'https://.*\.example\.org' 。
allow_methods -跨域请求应允许的HTTP方法列表。 默认为 ['GET'] 。 您可以使用 ['*'] 允许所有标准方法。
allow_headers -跨域请求应支持的HTTP请求标头列表。 默认为 [] 。 您可以 ['*'] 用来允许所有标头。 的 Accept ， Accept-Language ， Content-Language 和 Content-Type 头总是允许CORS请求。
allow_credentials -表示跨域请求应支持cookie。 默认为 False 。
expose_headers -指出应使浏览器可以访问的所有响应标头。 默认为 [] 。
max_age -设置浏览器缓存CORS响应的最长时间（以秒为单位）。 默认为 60 。
"""


@app.get("/")
async def main():
    return {"message": "Hello World"}


# GET访问：http://127.0.0.1:8000/
# 返回结果：
"""
{
    "message": "Hello World"
}
"""
# 暂时没有测试过跨域的不同
