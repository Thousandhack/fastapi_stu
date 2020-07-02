from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()


@app.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}


@app.get("/headers/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
自定义标头
请记住，可以使用'X-'前缀添加自定义专有标头。
但是，如果您希望浏览器中的客户端能够看到自定义标头，
则需要使用Starlette CORS中记录的参数将其添加到CORS配置（在CORS（跨源资源共享）中了解更多信息）。docs。
"""
