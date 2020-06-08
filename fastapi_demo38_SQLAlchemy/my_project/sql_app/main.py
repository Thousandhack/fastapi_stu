# https://www.pythonf.cn/read/56930
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# 作用是创建用户
# 例:POST请求：http://127.0.0.1:8000/users/
# body数据：
"""
{
	"email":"hsz@qq.com",
	"password":"hsz"
}
"""
# 返回结果：
"""
{
    "email": "hsz@qq.com",
    "id": 2,
    "is_active": true,
    "items": []
}
"""


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# 例子与说明：
# GET请求：http://127.0.0.1:8000/users/?skip=1&limit=5
# 返回结果：
"""
[
    {
        "email": "hsz@qq.com",
        "id": 2,
        "is_active": true,
        "items": []
    },
    {
        "email": "zero@qq.com",
        "id": 3,
        "is_active": true,
        "items": []
    }
]
"""


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# 例子：GET请求： http://127.0.0.1:8000/users/2/
# 返回结果：
"""
{
    "email": "hsz@qq.com",
    "id": 2,
    "is_active": true,
    "items": []
}
"""


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


# 主要作用是创建用户相应的Item
# POST请求：
# body数据：
"""
{
	"title":"今天6月8号"
}
"""
# 返回结果：
"""
{
    "title": "今天6月8号",
    "description": null,
    "id": 1,
    "owner_id": 2
}
"""


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


# 作用是查看item列表
# GET请求：

# 返回结果：http://127.0.0.1:8000/items/?skip=0&limit=5
"""
[
    {
        "title": "今天6月8号",
        "description": null,
        "id": 1,
        "owner_id": 2
    }
]
"""
