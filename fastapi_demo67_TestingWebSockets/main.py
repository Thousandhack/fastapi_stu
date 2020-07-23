from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    """
    使用websocket的测试工具进行测试：http://coolaf.com/tool/chattest
    ws://127.0.0.1:8000/ws
    返回结果大概：
    连接成功，现在你可以发送信息啦！！！
    服务端回应 2020-07-20 16:53:29
    {"msg": "Hello WebSocket"}
    websocket连接已断开!!!

    服务端打印为：
        INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
        INFO:     ('127.0.0.1', 64326) - "WebSocket /ws" [accepted]

    这个例子仅仅只能进行连接与断开的功能
    :param websocket:
    :return:
    """
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()


def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
