from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    """
    访问URL:   http://192.168.109.53:8000/items/3

    返回客户端ip
    item_id
    返回访问的基础路径
    返回访问的所有路径
    返回访问的方法
    :param item_id:
    :param request:
    :return:
    """
    client_host = request.client.host
    url = request.url
    method = request.method
    path = request.base_url

    return {"client_host": client_host,
            "item_id": item_id,
            "path": path,
            "url": url,
            "method": method}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
