from fastapi import Depends, FastAPI
import uvicorn

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


checker = FixedContentQueryChecker("bar")


@app.get("/query-checker/")
async def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

"""
FastApi教程|高级依赖
理解如下：
GET方法请求：
http://127.0.0.1:8000/query-checker/
返回结果：
{
    "fixed_content_in_query": true
}
FixedContentQueryChecker 类中可以知道，传入的"bar" 就是类中的实例化变量 fixed_content
如果在url中多q 的参数如果fixed_content 且bar值包含在q里面，返回的值 就会为True
所以以下访问都为True:
http://127.0.0.1:8000/query-checker/?q=bar
http://127.0.0.1:8000/query-checker/?q=bar_test
也就是q值包含bar返回的结果的键值对的bool值就为true


返回结果如下：
{
    "fixed_content_in_query": true
}

"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
