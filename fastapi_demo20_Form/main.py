from fastapi import FastAPI, Form
from starlette import status
from fastapi.responses import JSONResponse

app = FastAPI()

# form 表单的使用

@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    data = {"username": username, "password": password}
    res_data = {"code": -2, "data": data, "msg": "请求成功"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=res_data)


# POST请求：http://127.0.0.1:8000/login/
# body数据使用form-data，将数据传给后端
"""
username   zero
password   123456
"""
# 返回结果：后端对用户名和密码进行验证，返回相应的消息
"""
{
    "code": -2,
    "data": {
        "username": "zero",
        "password": "12345"
    },
    "msg": "请求成功"
}
"""
"""
注意：
可以 Form 在 路径操作中 声明多个 参数 ，但也不能声明 Body 希望以JSON形式接收的字段，
因为请求将使用 application/x-www-form-urlencoded 代替 编码主体 application/json 。
这不是 FastAPI 的限制 ，它是HTTP协议的一部分。
"""


