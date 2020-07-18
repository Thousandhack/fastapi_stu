from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}")
async def read_item(request: Request, id: str):
    """
    http://127.0.0.1:8000/items/6
    使用上面url访问返回对应的网页
    上面还有绿色的1号标题的内容：Item ID: 6
    :param request:
    :param id:
    :return:
    """
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
