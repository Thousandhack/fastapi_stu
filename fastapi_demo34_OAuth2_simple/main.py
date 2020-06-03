from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    """
    这边主要是实现通过token来获取用户信息，但是这边直接是用用户名来直接获取的用户信息，
    可以在get_user之前用token先获取用户id之类的东西，然后进行获取用户信息
    :param db:
    :param username:
    :return:
    """
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    print(user, "decode")
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


# 使用POST请求：http://127.0.0.1:8000/token
# 然后在form-data 提交请求数据：
"""
username    johndoe
password    secret
"""
# 返回结果：
"""
{
    "access_token": "johndoe",
    "token_type": "bearer"
}
"""


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


# 例1：
# GET请求： http://127.0.0.1:8000/users/me
# Header数据：
"""
Authorization   bearer alice
其中：Authorization   bearer为固定值
"""
# 返回结果：
"""
{
    "detail": "Inactive user"
}
"""

# 例2：
# GET请求：http://127.0.0.1:8000/users/me
# Header数据：
"""
Authorization   bearer johndoe
其中：Authorization   bearer为固定值
"""
# 返回结果：
"""
{
    "username": "johndoe",
    "email": "johndoe@example.com",
    "full_name": "John Doe",
    "disabled": false,
    "hashed_password": "fakehashedsecret"
}
"""

# 例子1的用户名是没有激活的，例子二的用户名是激活的
