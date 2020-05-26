from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    print(item)
    """
    title='test jsonble_encoder'
    timestamp=datetime.datetime(2008, 9, 15, 15, 53, tzinfo=datetime.timezone(datetime.timedelta(seconds=18000)))
    description='hhhh'
    """
    print(type(item))  # <class 'main.Item'>   # 一个对象的数据类型
    print(json_compatible_item_data)
    """
    {'title': 'test jsonble_encoder', 
    'timestamp': '2008-09-15T15:53:00+05:00', 
    'description': 'hhhh'}
    """
    print(type(json_compatible_item_data))  # 将从接口传过来的数据转换成字典的类型
    fake_db[id] = json_compatible_item_data

    return fake_db[id]


# jsonable_encoder 实际上由 FastAPI在 内部用于转换数据。

# 这个确实挺重要，当传来的数据，只是的单个数据的时候可以获取

# 例子：
# PUT请求：http://127.0.0.1:8000/items/dd
# body数据
"""
{
	"title":"test jsonble_encoder",
	"timestamp":"2008-09-15T15:53:00+05:00",
	"description":"hhhh"
}
"""

# 返回数据：
"""
{
    "title": "test jsonble_encoder",
    "timestamp": "2008-09-15T15:53:00+05:00",
    "description": "hhhh"
}
"""
