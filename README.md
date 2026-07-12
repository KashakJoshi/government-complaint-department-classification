Government Complaint Department Classification System

Overview

This project is an AI-based complaint classification system that predicts the correct government department from user complaints.

The system supports:
- Text complaints
- Image complaints using OCR
- Audio complaints using Speech-to-Text

All inputs are converted into Hindi text and processed by a trained BERT classification model to predict the department.


## Workflow

Input (Text / Image / Audio)

↓

Text Extraction  
(OCR for Image, Whisper for Audio)

↓

Hindi Text Processing

↓

BERT Classification Model

↓

Department Prediction


## Models & Technologies Used

Machine Learning:
- Fine-tuned BERT Model
- PyTorch
- Transformers

OCR:
- EasyOCR

Audio Processing:
- OpenAI Whisper

API:
- FastAPI
- Uvicorn


## Project Structure

```
api/
 └── main1.py

src/
 ├── predict.py
 └── components/
     ├── input_router.py
     ├── ocr_processor.py
     └── audio_processor.py

models/
 ├── best_model.pt
 ├── tokenizer
 └── label_mapping.json
```


## How to Run API

1. Activate virtual environment:

```bash
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start FastAPI server:

```bash
python -m uvicorn api.main1:app --reload
```

4. Open Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

From Swagger UI, text, image and audio complaint predictions can be tested.