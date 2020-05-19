from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()

# 挂载模板文件夹
tmp = Jinja2Templates(directory='templates')


@app.get('/')  # 接受get请求
async def get_file(request: Request):
    return tmp.TemplateResponse('file.html', {'request': request})


# 单个文件
@app.post("/uploadfile/")
async def create_upload_file(request: Request,
                             file: UploadFile = File(...),
                             # files: bytes = File(...),  # # 把文件对象转为bytes类型,这种类型的文件无法保存
                             # info: str = Form(...)  # 获取普通键值对
                             ):
    # 保存上传的文件
    contents = await file.read()
    with open("file/" + file.filename, "wb") as f:
        f.write(contents)
    # return {"filename": file.filename}
    return tmp.TemplateResponse('index.html', {
        'request': request,
        # 'file_size': len(files),
        'file_name': file.filename,
        # 'info': info,
        'file_content_type': file.content_type
    })


# 多个文件  暂时失败
@app.post('/files/')
async def get_files(files_obj_list: List[UploadFile] = File(...)  # [file_obj1,file_obj2,....] # 文件框里可以同时上传多个文件
                    ):
    # 保存上传的多个文件
    for file in files_obj_list:
        contents = await file.read()
        filename = file.filename
        with open("file/" + filename, "wb") as f:
            f.write(contents)

    return "2222"
    # return tmp.TemplateResponse('index.html',
    #                             {'request': request,
    #                              # 'file_sizes': [len(file) for file in files_list],
    #                              'file_names': [file_obj.filename for file_obj in files_obj_list]
    #                              }
    #                             )
