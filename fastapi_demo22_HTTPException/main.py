from fastapi import FastAPI, HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse


# 使用 from starlette.requests import Request
# 和 from starlette.responses import JSONResponse

# demo03 自定义处理异常
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="id not found")
    return {"item": items[item_id]}


# GET请求： http://127.0.0.1:8000/items/ddd
# 返回 404
"""
结果：
{
    "detail": "Not Found"
}
"""


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


# 返回结果同上，但是暂时不知道有什么区别


# demo03的例子：自定义异常处理


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# GET请求： http://127.0.0.1:8000/unicorns/yolo
# 返回结果: 状态码： 418I'm a teapot (RFC 2324)
"""
{
    "message": "Oops! yolo did something. There goes a rainbow..."
}
"""

# demo04: 重写 HTTPException 错误处理程序
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/demo05/{demo05_id}")
async def read_item(demo05_id: int):
    if demo05_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": demo05_id}


# demo05
# GET请求1：http://127.0.0.1:8000/demo05/eee
# 返回结果： 400Bad Request
# 返回结果消息：
"""
1 validation error for Request
path -> demo05_id
  value is not a valid integer (type=type_error.integer)
"""

# GET请求2; http://127.0.0.1:8000/demo05/3  抛出自己定义的异常处理
"""
返回系统状态码： 418I'm a teapot (RFC 2324)
Nope! I don't like 3.
"""
# GET请求3：http://127.0.0.1:8000/demo05/5   正确请求的情况

# 返回结果:
"""
{
    "item_id": 5
}
"""
