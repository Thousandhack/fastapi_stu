from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse

app = FastAPI()


# 调用ORJSONResponse 需要安装： pip install orjson

@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]


# 在这种情况下，HTTP请求头 Content-Type 将设置为 application/json 。  系统默认的请求头
# 请求的需要的类型可以在docs中提现 也就是 OpenAPI

@app.get("/return_html/", response_class=HTMLResponse)
async def return_html():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ! HTML!</h1>
        </body>
    </html>
    """


# GET请求浏览器测试：http://127.0.0.1:8000/return_html/
# 返回html渲染后的数据


@app.get("/text/", response_class=PlainTextResponse)
async def text():
    return "Hello World"


# GET请求：http://127.0.0.1:8000/text/
# 返回text类型的数据

# 在这种情况下，HTTP请求头 Content-Type 将设置为 text/html 。
# 请求的需要的类型可以在docs中提现

"""
RedirectResponse
返回HTTP重定向。 默认情况下使用307状态代码（临时重定向）
"""


@app.get("/redirect_typer/")
async def redirect():
    return RedirectResponse("https://typer.tiangolo.com")

# GET请求访问： http://127.0.0.1:8000/redirect_typer/
# 会重定向到网站：https://typer.tiangolo.com


async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"


@app.get("/fake_video/")
async def fake_video():
    return StreamingResponse(fake_video_streamer())

# GET请求：http://127.0.0.1:8000/fake_video/
# 具体没有理解很好！！！！

"""
使用 StreamingResponse 与类文件对象
如果您有类似文件的对象（例如 open() ） 返回的对象 ，则可以在中将其返回 StreamingResponse 。

其中包括许多与云存储，视频处理等交互的库。
"""

some_file_path = "user_data.xls"


@app.get("/file/")
async def file():
    return FileResponse(some_file_path)

"""
GET请求：http://127.0.0.1:8000/file/
结果是将文件下载到本地
"""
