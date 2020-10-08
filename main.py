from fastapi import FastAPI, File, UploadFile
import shutil
import cv2 as cv
import numpy as np

app = FastAPI()

'''
https://fastapi.tiangolo.com/tutorial/background-tasks/
https://levelup.gitconnected.com/how-to-save-uploaded-files-in-fastapi-90786851f1d3
'''
@app.get("/hello/")
async def root():
    return {"message": "Hello World"}
    

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    # Load an color image in grayscale
    img = cv.imread(file.filename, 0)    
   
    return {"filename": file.filename, 'file_size': file.content_type}

