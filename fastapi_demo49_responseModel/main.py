from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
import os


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


app = FastAPI()


@app.get("/items1/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item1(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        # 下面可以自定义返回状态码和消息
        return JSONResponse(status_code=400, content={"message": "Item_id not found"})


"""
GET请求：http://127.0.0.1:8000/items1/foo/
返回：
{
    "id": "foo",
    "value": "there goes my hero"
}
"""


@app.get(
    "/items2/{item_id}",
    response_model=Item,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
async def read_item2(item_id: str, img: bool = None):
    if img:
        # print(item_id)
        res = os.path.exists("img.jpg")  # 判断img.jpg是否在当前目录下，也就是运行文件的目录下
        if not res:
            return JSONResponse(status_code=400, content={"message": "Item_id not found"})
        print("hhhh")
        # 返回当前目录下的文件：img.jpg 文件   文件的类型可以为：image或png类型
        return FileResponse("zero.png", media_type="image/png")
    else:
        return {"id": item_id, "value": "there goes my hero"}


"""
测试1：
GET请求：http://127.0.0.1:8000/items2/f/   
后面的item_id 随意
返回结果：
{   "id":"f",
    "value":"there goes my hero"
}

测试2：
GET请求：http://127.0.0.1:8000/items2/f/?img=1
返回结果为：返回一个文件
 return FileResponse("img.jpg", media_type="image/png")
 上面一句代码表示：返回当前目录下的文件：img.jpg 文件   文件的类型可以为：image或png类型
"""


@app.get(
    "/items3/{item_id}",
    response_model=Item,
    responses={
        404: {"model": Message, "description": "The item was not found"},
        200: {
            "description": "Item requested by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "The bar tenders"}
                }
            },
        },
    },
)
async def read_item3(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

"""
测试：
返回结果：http://127.0.0.1:8000/items3/foo
{"id":"foo","value":"there goes my hero"}

意思get方法内的responses 的例子都可以在docs
也就是全部组合并包含在OpenAPI中
"""
