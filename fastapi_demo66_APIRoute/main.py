import gzip
from typing import Callable, List

from fastapi import Body, FastAPI, Request, Response
from fastapi.routing import APIRoute


class GzipRequest(Request):
    async def body(self) -> bytes:
        if not hasattr(self, "_body"):
            body = await super().body()
            if "gzip" in self.headers.getlist("Content-Encoding"):
                body = gzip.decompress(body)
            self._body = body
        return self._body


class GzipRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = GzipRequest(request.scope, request.receive)
            return await original_route_handler(request)

        return custom_route_handler

"""
创建自定义 GzipRoute 类
接下来，我们将创建一个自定义子类 fastapi.routing.APIRoute ，以使用 GzipRequest 。
这次，它将覆盖方法 APIRoute.get_route_handler() 。
此方法返回一个函数。 该函数将接收请求并返回响应。
在这里，我们使用它 GzipRequest 从原始请求中 创建一个 。
"""

app = FastAPI()
app.router.route_class = GzipRoute


@app.post("/sum")
async def sum_numbers(numbers: List[int] = Body(...)):
    return {"sum": sum(numbers)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
