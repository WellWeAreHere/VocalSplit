from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from services.demucs_services import separate_audio
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], #trust this shit 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/") #RUN ROOT if u r in this URL 
def root():
    return {"message": "Backend is running 🚀"}


@app.post("/upload")
def upload_song(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_folder = separate_audio(file_path)

    return {
        "message": "Upload and separation successful!",
        "filename": file.filename,
        "output": output_folder,
    }