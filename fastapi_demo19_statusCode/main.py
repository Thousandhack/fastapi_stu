from fastapi import FastAPI
# from fastapi import status
from starlette import status
app = FastAPI()


@app.post("/demo01/", status_code=201)
async def create_item(name: str):
    return {"name": name}


#
# POST请求：http://127.0.0.1:8000/demo01/?name=one
# 返回结果：相应系统状态码：201Created
"""
{
    "name": "one"
}
"""


@app.post("/demo02/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


# 和demo01的效果是一样的
from fastapi.responses import JSONResponse


# demo03为自定义的状态码后面回复的数据为：
@app.post("/demo03/")  # , status_code=status.HTTP_201_CREATED
async def create_data(name):
    data = {"name": name}
    res_data = {"code": -2, "data": data, "msg": "请求成功"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=res_data)

# POST请求： http://127.0.0.1:8000/demo03/?name=THREE
# 返回结果：
"""
{
    "code": -2,
    "data": {
        "name": "THREE"
    },
    "msg": "请求成功"
}
"""


