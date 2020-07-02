from fastapi import FastAPI, Response, status
import uvicorn

app = FastAPI()

tasks = {"foo": "Listen to the Bar Fighters"}


@app.put("/get-or-create-task/{task_id}", status_code=200)
def get_or_create_task(task_id: str, response: Response):
    if task_id not in tasks:
        tasks[task_id] = "This didn't exist before"
        response.status_code = status.HTTP_201_CREATED
    return tasks[task_id]

"""
首先是访问的PUT方法
http://127.0.0.1:8000/get-or-create-task/zero/ 
然后是当最后的task_id 没有的时候 返回的系统状态码改变为 201
返回的消息也改变了  "This didn't exist before"
当访问task_id 存在的时候返回：系统状态码 200
返回消息："Listen to the Bar Fighters"  也就是task_id 键对应的值
"""


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
