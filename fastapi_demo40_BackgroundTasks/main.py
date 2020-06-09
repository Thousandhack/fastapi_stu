from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    """
    作用大概是将邮件地址和内容记录在日志中
    :param email:
    :param message:
    :return:
    """
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


# POST请求：http://127.0.0.1:8000/send-notification/123@qq.com
# 返回结果：里面会有日志记录功能
"""
{
    "message": "Notification sent in the background"
}
"""

"""
理解还不够深，后台任务还不知道怎么使用
"""

"""
警告
如果您需要执行大量的后台计算，而不必一定要在同一进程中运行它（例如，您不需要共享内存，变量等），则可能会受益于使用其他更大的工具，例如 芹菜 。

它们往往需要更复杂的配置，例如RabbitMQ或Redis之类的消息/作业队列管理器，但是它们允许您在多个进程（尤其是多个服务器）中运行后台任务。

要查看示例，请检查 Project Generators ，它们都包括已经配置的Celery。

但是，如果您需要从同一 FastAPI 应用 访问变量和对象 ，或者需要执行一些小的后台任务（例如发送电子邮件通知），则只需使用即可 BackgroundTasks 。
"""
