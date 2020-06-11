from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]


@app.get("/items_two/", include_in_schema=False)  # 这项配置就是可以将接口禁用：include_in_schema=False
async def read_items():
    return [{"item_id": "Foo"}]


"""
本demo主要是路径操作高级配置
从OpenAPI排除
要将 路径操作 从生成的OpenAPI架构（以及自动文档系统）中 排除 ，请使用参数 include_in_schema 并将其设置为 False
# 也就是自定义 OpenAPI的operationId
访问docs里面： http://127.0.0.1:8008/docs#/default/some_specific_id_you_define

"""
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)
