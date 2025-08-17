from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from services.whisper_service import transcribe_audio
from services.gpt_service import generate_script
from services.video_editor import create_video

app = FastAPI()

# Allow frontend (React) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static folder exists
os.makedirs("static", exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Whisper transcription
    transcript = transcribe_audio(file_location)

    # GPT script generation
    script = generate_script(transcript)

    # Video generation
    video_path = create_video(file_location)

    return {
        "transcript": transcript,
        "script": script,
        "video_url": f"/static/{os.path.basename(video_path)}"
    }