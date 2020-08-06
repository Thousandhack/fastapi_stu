from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


def custom_openapi():
    """
    您可以将该属性.openapi_schema用作“缓存”，以存储生成的模式。
    这样，您的应用程序不必在用户每次打开API文档时都生成架构。
    它只会生成一次，然后相同的缓存模式将用于下一个请求。
    :return:
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    # 可以添加ReDoc扩展，向OpenAPI模式中x-logo的info“对象” 添加自定义
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/icon-white.svg",
        # "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

"""
访问这个：http://127.0.0.1:8000/redoc
可知修改了哪些信息
"""
