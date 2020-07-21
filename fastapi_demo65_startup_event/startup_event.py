from fastapi import FastAPI

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    """
    startup-----
    INFO:     Started server process [12080]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
    以上为程序运行后的打印
    :return:
    """
    print("startup-----")
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
