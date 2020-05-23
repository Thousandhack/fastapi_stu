"""
其他数据类型
以下是一些您可以使用的其他数据类型：

UUID ：
一个标准的“通用唯一标识符”，在许多数据库和系统中通常作为ID使用。
在请求和响应中将以表示 str 。

datetime.datetime ：
一个Python datetime.datetime 。
在请求和响应中，将以 str ISO 8601格式表示，例如： 2008-09-15T15:53:00+05:00 。

datetime.date ：
Python datetime.date 。
在请求和响应中，将以 str ISO 8601格式表示，例如： 2008-09-15 。

datetime.time ：
一个Python datetime.time 。
在请求和响应中，将以 str ISO 8601格式表示，例如： 14:23:55.003 。

datetime.timedelta ：
一个Python datetime.timedelta 。
在请求和响应中，将以 float 总秒数表示。
Pydantic还允许将其表示为“ ISO 8601时间差异编码”， 有关更多信息 ， 请参阅文档 。

frozenset ：
在请求和响应中，将与视为相同 set ：
在请求中，将读取列表，消除重复，并将其转换为 set 。
作为响应， set 将会转换为 list 。
生成的架构将指定 set 值是唯一的（使用JSON架构的 uniqueItems ）。

bytes ：
标准Python bytes 。
在请求和响应中将被视为 str 。
生成的模式将指定，这是一个 str 与 binary “格式”。

Decimal ：
标准Python Decimal 。
在请求和响应中，处理方式与相同 float 。
"""

from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.post("/items/{item_id}")
async def read_items(
        item_id: int,
        start_datetime: datetime = Body(None),
        # end_datetime: datetime = Body(None),
        # repeat_at: time = Body(None),
        # process_after: timedelta = Body(None),
):
    # start_process = start_datetime + process_after
    # duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": datetime.now(),
        # "repeat_at": repeat_at,
        # "process_after": process_after,
        # "start_process": start_process,
        # "duration": duration,
    }

# 时间这块没搞定

# https://www.pythonf.cn/read/56903
