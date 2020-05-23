from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(*, ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}

# FastApi教程|Cookie参数
# https://www.pythonf.cn/read/56904
# 例子没有弄明白

