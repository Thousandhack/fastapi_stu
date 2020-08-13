from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
"""
禁用自动文档
第一步是禁用自动文档，因为默认情况下会使用CDN。
要禁用它们，请 None 在创建 FastAPI 应用程序 时 将其URL设置
"""
app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")

"""
您可以重复使用FastAPI的内部函数来为文档创建HTML页面，并将所需的参数传递给它们：

openapi_url ：文档HTML页面可在其中获取API的OpenAPI架构的URL。 您可以在此处使用属性 app.openapi_url 。
title ：您的API的标题。
oauth2_redirect_url ：您可以 app.swagger_ui_oauth2_redirect_url 在此处使用默认值。
swagger_js_url ：Swagger UI文档的HTML可以从中获取 JavaScript 文件 的URL 。 这是您自己的应用程序现在正在提供的应用程序。
swagger_css_url ：Swagger UI文档的HTML可以从中获取 CSS 文件 的URL 。 这是您自己的应用程序现在正在提供的应用程序。
对于ReDoc同样如此...
"""
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


@app.get("/users/{username}")
async def read_user(username: str):
    """
    访问：http://127.0.0.1:8000/users/hsz
    返回结果：
        {"message":"Hello hsz"}
    :param username:
    :return:
    """
    return {"message": f"Hello {username}"}



# uvicorn app.main:app --reload  --host=0.0.0.0 --port=800
