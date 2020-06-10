from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
"""
细节
第一个 "/static" 引用此“子应用程序”将被“挂载”的子路径。 因此，任何以它开头的路径 "/static" 都将被它处理。
该 directory="static" 指包含你的静态文件的目录名。
该 name="static" 给它可以通过内部使用的名称 FastAPI 。
所有这些参数都可以与“ static ” 不同 ，并根据您自己的应用程序的需求和特定细节进行调整。
"""
