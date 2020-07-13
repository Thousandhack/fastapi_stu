from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}

"""
例子：
使用浏览器进行访问
http://127.0.0.1:8000/users/me
弹出一个需要填写账号和密码的框
填写完成
返回：
{"username":"admin","password":"123456"}

如果是docs中还可以进行退出的操作
"""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
