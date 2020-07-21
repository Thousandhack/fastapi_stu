from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/app")
def read_main():
    """
    此接口只能由：
    http://127.0.0.1:8000/app
    进行访问，并没有被注册或挂载到子应用
    在默认的 http://127.0.0.1:8000/docs中 打开文档也可以找到
    :return:
    """
    return {"message": "Hello World from main app"}


# openapi_prefix 在 FastAPI 应用程序中 声明一个 参数
# 创建子应用
subapi = FastAPI(openapi_prefix="/subAPI")
test = FastAPI(openapi_prefix="/subTEST")


# 注意这边不在是app 了
# 而且可以挂载到多个子应用上
@subapi.get("/sub")
@test.get("/sub")
def read_sub():
    """
    这个接口已经被注册挂载到子应用上
    访问url为：
        http://127.0.0.1:8000/subAPI/sub
    :return:
    """
    return {"message": "Hello World from sub API"}


# 需要进行挂载才能生效
# 挂载子应用
app.mount("/subAPI", subapi)
app.mount("/subTEST", test)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# 1. session加密的时候已经配置过了.如果没有在配置项中设置,则如下:
app.secret_key = "sdqwoqn132u01bdxye82BIBIdho"  # 此处可以写随机字符串#


