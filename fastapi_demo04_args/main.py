from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    hsz = "hhhh"


app = FastAPI()


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# 访问：
# http://127.0.0.1:8000/model/alexnet/
# 返回：
# {
#     "model_name": "alexnet",
#     "message": "Deep Learning FTW!"
# }

# 访问：
# http://127.0.0.1:8000/model/lenet/

# 返回：
# {
#     "model_name": "lenet",
#     "message": "LeCNN all the images"
# }


# 访问：http://127.0.0.1:8000/model/resnet/
# 返回：
# {
#     "model_name": "resnet",
#     "message": "Have some residuals"
# }

# 访问： http://127.0.0.1:8000/model/hhhh/
# 返回：
# {
#     "model_name": "hhhh",
#     "message": "Have some residuals"
# }
