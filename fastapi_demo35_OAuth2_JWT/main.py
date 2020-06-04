"""
关于 JWT
JWT的意思是“ JSON Web令牌”
如果您想使用JWT令牌并查看它们如何工作，请查看 https://jwt.io 。
pip install pyjwt
"""

"""
密码哈希
“散列”是指将某些内容（在这种情况下为密码）转换为看起来像乱七八糟的字节序列（只是一个字符串）。

每当您传递完全相同的内容（完全相同的密码）时，您都会得到完全相同的胡言乱语。

但是您不能从乱码转换回密码。

为什么要使用密码哈希
如果您的数据库被盗，小偷将没有用户的明文密码，只有哈希值。

因此，小偷将无法尝试在另一个系统中使用该密码（由于许多用户在各处都使用相同的密码，因此很危险）。

安装 passlib
PassLib是一个很棒的Python程序包，用于处理密码哈希。

它支持许多安全的哈希算法和实用程序来使用它们。

推荐的算法是“ Bcrypt”。

因此，使用Bcrypt安装PassLib：

pip install passlib[bcrypt]
"""

from datetime import datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext  # PassLib“上下文”
from pydantic import BaseModel

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  # token加密的密钥
ALGORITHM = "HS256"  # 加密的方法
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 访问token设置的过期时间

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app = FastAPI()


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    生成hash的密码
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 产生一个访问token 之后有数据库了，那么在这边可以先进行判断token是否过期，如果过期再生成新的token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


"""
# 主要作用大概是用户登录，返回相应的token
POST请求:http://127.0.0.1:8000/token
# 然后在form-data 提交请求数据：
username    johndoe
password    secret
# 返回数据：
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNTkxMTQ4MDc0fQ.ocZ-c2XhhebefQn_ql0nceV6ZPMD1Q6aT5cZ_zSumQk",
    "token_type": "bearer"
}

"""


@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


# 例2：
# GET请求：http://127.0.0.1:8000/users/me
# Header数据：
"""
Authorization   bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNTkxMTQ4MDc0fQ.ocZ-c2XhhebefQn_ql0nceV6ZPMD1Q6aT5cZ_zSumQk
其中：Authorization   bearer为固定值 后面为jwt token的的值
"""
# 返回结果：根据token返回当前用户信息
"""
{
    "username": "johndoe",
    "email": "johndoe@example.com",
    "full_name": "John Doe",
    "disabled": false
}
"""


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return {"item_id": "Foo", "owner": current_user.username}

# 例3：GET请求： http://127.0.0.1:8000/users/me/items/
# Header数据：
"""
Authorization   bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNTkxMTQ4MDc0fQ.ocZ-c2XhhebefQn_ql0nceV6ZPMD1Q6aT5cZ_zSumQk
其中：Authorization   bearer为固定值 后面为jwt token的的值
"""
# 返回结果：
"""
{
    "item_id": "Foo",
    "owner": "johndoe"
}
"""
