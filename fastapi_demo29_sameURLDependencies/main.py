from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

# 首先注意：x_token  在请求头是不可行的，请求头只有中线。
# 例子：http://127.0.0.1:8000/items/
# 请求头内容：
"""
x-token
fake-super-secret-token

x-key
fake-super-secret-key
"""
# 返回结果：
"""
[
    {
        "item": "Foo"
    },
    {
        "item": "Bar"
    }
]
"""

