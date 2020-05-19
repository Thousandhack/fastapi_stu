from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def read_item(item_id: int, q: str = None):
    if q == "666":
        print("触发了吗")
        return JSONResponse(status_code=400, content=q)
    return {"item_id": item_id, "q": q}


@app.get("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
