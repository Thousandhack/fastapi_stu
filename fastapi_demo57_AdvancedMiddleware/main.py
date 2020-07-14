from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import uvicorn

app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
"""
HTTPSRedirectMiddleware
强制所有传入请求必须为 https 或 wss。
"""

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com", "127.0.0.1"]
)
"""
TrustedHostMiddleware
强制所有传入请求都具有正确设置的 Host 标头，以防止受到HTTP Host Header攻击。
允许任何主机名使用 allowed_hosts=["*"] 或省略中间件。
"""
app.add_middleware(GZipMiddleware, minimum_size=1000)

"""
这个中间件暂时没有测试到效果
手柄GZIP用于包括任何请求响应"gzip"中的Accept-Encoding报头。
中间件将处理标准响应和流响应。
minimum_size-不要GZip响应小于此最小大小（以字节为单位）。默认为500。
"""


@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
