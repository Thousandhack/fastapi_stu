from fastapi import FastAPI

app = FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    """
    使用命令运行起次程序：
    uvicorn shutdown_event:app --reload  --host=0.0.0.0 --port=8000
    然后进行正常的访问后Ctrl+c 结束其程序后打印如下：

    ?[32mINFO?[0m:     127.0.0.1:58273 - "?[1mGET /items/foo HTTP/1.1?[0m" ?[31m404 Not Found?[0m
    ?[32mINFO?[0m:     127.0.0.1:58274 - "?[1mGET /items/ HTTP/1.1?[0m" ?[32m200 OK?[0m
    ?[32mINFO?[0m:     Shutting down
    ?[32mINFO?[0m:     Waiting for application shutdown.
    shutdown--------
    ?[32mINFO?[0m:     Application shutdown complete.
    ?[32mINFO?[0m:     Finished server process [?[36m17848?[0m]
    ?[31mERROR?[0m:    Could not stop child process 17848: [WinError 5] 拒绝访问。
    ?[32mINFO?[0m:     Stopping reloader process [?[36m?[1m22876?[0m]

    :return:
    """
    print('shutdown--------')
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
