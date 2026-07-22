import uuid
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from services.demucs_services import separate_audio
import shutil
import os
jobs = {}
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


def process_song(job_id: str, file_path: str):
    separate_audio(file_path)
    jobs[job_id] = "completed"


@app.post("/upload")
def upload_song(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):   
    job_id = str(uuid.uuid4())
    jobs[job_id] = "processing"
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(
    process_song,
    job_id,
    file_path
)

    return {
        "job_id": job_id,
        "status": "processing"
    }

@app.get("/status/{job_id}")
def get_status(job_id: str):
    return {
        "status": jobs.get(job_id, "not found")
    }