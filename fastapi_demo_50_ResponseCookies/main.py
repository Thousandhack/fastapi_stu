from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/cookie-and-object/")
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value-test1")
    return {"message": "Come to the dark side, we have cookies"}


# Post请求：http://127.0.0.1:8000/cookie-and-object/
# 返回结果：
# Cookies返回了key="fakesession", value="fake-cookie-session-value-test1"
# body返回的结果：
# {
#     "message": "Come to the dark side, we have cookies"
# }

@app.post("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response

# post请求：http://127.0.0.1:8000/cookie/
# 返回结果：
"""
{
    "message": "Come to the dark side, we have cookies"
}
然后在Cookies返回了
key="fakesession", value="fake-cookie-session-value" 的Cookies数据
"""

"""
Response 直接在代码中返回时,创建cookie 。
可以按照直接返回 响应中所述创建响应 。
然后在其中设置Cookies
"""
