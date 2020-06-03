from typing import Optional

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


# GET请求: http://127.0.0.1:8000/users/me
# header 请求头数据：
"""
Authorization  bearer 1111
"""

# 返回数据结果：
"""
{
    "username": "1111fakedecoded",
    "email": "john@example.com",
    "full_name": "John Doe",
    "disabled": null
}
"""


# 创建 get_current_user 依赖 返回当前用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/demo02/me")
async def read_demo02_me(current_user: User = Depends(get_current_user)):
    return current_user

# get请求：http://127.0.0.1:8000/demo02/me
"""
Authorization  bearer zero
"""
# 返回数据结果：
"""
{
    "username": "zerofakedecoded",
    "email": "john@example.com",
    "full_name": "John Doe",
    "disabled": null
}
"""
