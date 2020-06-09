from fastapi import FastAPI

# app = FastAPI(
#     title="My Super Project",
#     description="This is a very fancy project, with auto docs for the API and everything",
#     version="2.5.0",
# )
"""
访问：http://127.0.0.1:8000/docs
显示的标题还有说明和版本是根据上面的配置来显示的
"""

# app = FastAPI(openapi_url="/api/v1/openapi.json")

# 原来的默认位置为：http://127.0.0.1:8000/openapi.json
# 以上配置修改为：http://127.0.0.1:8000/api/v1/openapi.json


app = FastAPI(docs_url="/documentation", redoc_url=None)

# 配置效果就是将docs API接口文档解释的访问位置改为： http://127.0.0.1:8000/documentation
# 并禁用：http://127.0.0.1:8000/redoc


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
