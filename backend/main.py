from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/") #RUN ROOT if u r in this URL 
def root():
    return {"message": "Backend is running 🚀"}


@app.post("/upload") #RUN the fucntion below if in this URL 
def upload_song(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Upload successful!",
        "filename": file.filename,
    }