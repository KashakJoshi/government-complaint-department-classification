from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from src.predict import predict_department
from src.components.ocr_processor import process_image
from src.components.audio_processor import process_audio


app = FastAPI(
    title="Complaint Classification API",
    description="Hindi Complaint Department Classification API",
    version="1.0"
)


UPLOAD_DIR = "data/input"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


class TextRequest(BaseModel):

    text: str



@app.get("/")
def home():

    return {
        "message": "Complaint Classification API Running"
    }



# =====================
# TEXT PREDICTION
# =====================

@app.post("/predict/text")
def predict_text(
    request: TextRequest
):

    result = predict_department(
        request.text
    )

    return {
        "input_type": "text",
        "complaint": request.text,
        "prediction": result
    }



# =====================
# IMAGE PREDICTION
# =====================

@app.post("/predict/image")
async def predict_image(
    file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = process_image(
        file_path
    )

    return {
        "input_type": "image",
        "file": file.filename,
        "prediction": result
    }



# =====================
# AUDIO PREDICTION
# =====================

@app.post("/predict/audio")
async def predict_audio(
    file: UploadFile = File(...)
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = process_audio(
        file_path
    )

    return {
        "input_type": "audio",
        "file": file.filename,
        "prediction": result
    }