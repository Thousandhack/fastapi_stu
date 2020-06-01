from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# 需要安装： pip install python-multipart

@app.get("/demo01/")
async def read_demo01(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# 请求例子： http://127.0.0.1:8000/demo01/
# 返回结果：也就是没有认证的意思
"""
{
    "detail": "Not authenticated"
}
"""

# 请求例子2：http://127.0.0.1:8000/demo01/
# header 数据为：
"""
Authorization    bearer 1111
"""
# 返回结果：
"""
{
    "token": "1111"
}
"""
