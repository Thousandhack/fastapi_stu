from fastapi import FastAPI, Header
from typing import List

app = FastAPI()


@app.get("/items/")
async def read_items(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}


# 请求：http://127.0.0.1:8000/items/

# 浏览器请求返回结果： {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

# postman请求返回结果： { "User-Agent": "PostmanRuntime/7.24.1" }


@app.get("/demo02/")
async def read_items(*, strange_header: str = Header(None, convert_underscores=False)):
    return {"strange_header": strange_header}


# 请求： http://127.0.0.1:8000/demo02/
# 在Headers 加键值对如下：
"""
strange_header     345678767test    
"""

# 返回结果：
"""
{
    "strange_header": "345678767test"
}
"""


# 标头重复
@app.get("/demo03/")
async def read_items(x_token: List[str] = Header(None)):
    return {"X-Token values": x_token}

# 请求：http://127.0.0.1:8000/demo03/
# 在Headers下面加两个相同键值对如下：
"""
X-Token    test0001
X-Token    test0002
"""

# 返回结果：
"""
{
    "X-Token values": [
        "test0001",
        "test0002"
    ]
}
"""
