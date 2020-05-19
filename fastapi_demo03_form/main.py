from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(*, username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

# 访问地址
# http://127.0.0.1:8000/login/
# form-data 上添加  username 和 password 键值对
